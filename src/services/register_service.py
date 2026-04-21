# services/register_service.py

from models.field import Field
from models.fertilizer_application import FertilizerApplication
from models.production_record import ProductionRecord
from utils.validators import (
    get_non_empty_string,
    get_positive_float,
    get_confirmation,
    get_valid_field_id
)
from data.json_manager import load_data, save_data
from data.txt_manager import write_log
from data.oracle_manager import (
    insert_field,
    insert_fertilizer_application,
    insert_production_record,
    delete_field_from_oracle,
    delete_fertilizer_applications_by_field_id,
    delete_production_records_by_field_id,
    list_fields_from_oracle,
    list_fertilizer_applications_from_oracle,
    list_production_records_from_oracle
)
from utils.helpers import generate_next_id
from utils.formatters import (
    print_title,
    print_subtitle,
    print_separator,
    print_empty_message,
    print_key_value
)

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def register_field():
    """
    Registers a new field and saves it to a JSON file and Oracle database.
    """
    print("\n=== CADASTRO DE TALHÃO ===")

    name = get_non_empty_string("Digite o nome do talhão: ")
    area = get_positive_float("Digite a área do talhão em hectares: ")
    crop_type = get_non_empty_string("Digite a cultura plantada: ")

    fields = load_data(FIELDS_FILE_PATH)

    field_id = generate_next_id(fields, "field_id")
    new_field = Field(field_id, name, area, crop_type)

    fields.append(new_field.to_dict())
    save_data(FIELDS_FILE_PATH, fields)

    oracle_success, oracle_message = insert_field(new_field.to_dict())

    print("\nTalhão cadastrado com sucesso!")
    print(oracle_message)

    write_log(
        "FIELD_REGISTERED",
        f"Field ID {field_id} registered - Name: {name}, Area: {area}, Crop: {crop_type}"
    )

def list_fields():
    """
    Displays all registered fields from JSON and Oracle.
    """

    print_title("Talhões em JSON")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print_empty_message("Nenhum talhão cadastrado no JSON.")
    else:
        for field in fields:
            print_separator()
            print_key_value("ID", field["field_id"])
            print_key_value("Nome", field["name"])
            print_key_value("Área (ha)", field["area"])
            print_key_value("Cultura", field["crop_type"])

    print_title("Talhões no Oracle")

    oracle_success, oracle_result = list_fields_from_oracle()

    if not oracle_success:
        print_empty_message(oracle_result)
        return

    if not oracle_result:
        print_empty_message("Nenhum talhão cadastrado no Oracle.")
        return

    for row in oracle_result:
        print_separator()
        print_key_value("ID", row[0])
        print_key_value("Nome", row[1])
        print_key_value("Área (ha)", row[2])
        print_key_value("Cultura", row[3])

def delete_field():
    """
    Deletes a field and all related fertilizer applications and production records.
    IDs are not reorganized after deletion.
    """
    print("\n=== EXCLUSÃO DE TALHÃO ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado.")
        return

    for field in fields:
        print(f"\nID: {field['field_id']} - Nome: {field['name']}")

    try:
        field_id = int(input("\nDigite o ID do talhão que deseja excluir: "))
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        return

    field_to_delete = None
    for field in fields:
        if field["field_id"] == field_id:
            field_to_delete = field
            break

    if not field_to_delete:
        print("Talhão não encontrado.")
        return

    applications = load_data(APPLICATIONS_FILE_PATH)
    production_records = load_data(PRODUCTION_FILE_PATH)

    related_applications = [
        application for application in applications
        if application["field_id"] == field_id
    ]

    related_production_records = [
        record for record in production_records
        if record["field_id"] == field_id
    ]

    print("\nOs seguintes dados serão excluídos:")
    print(f"- Talhão: {field_to_delete['name']}")
    print(f"- Aplicações de fertilizante vinculadas: {len(related_applications)}")
    print(f"- Registros de produção vinculados: {len(related_production_records)}")

    confirm = get_confirmation(
        "\nTem certeza que deseja continuar com a exclusão em cascata? (s/n): "
    )

    if not confirm:
        print("Exclusão cancelada.")
        return

    updated_fields = [
        field for field in fields
        if field["field_id"] != field_id
    ]

    updated_applications = [
        application for application in applications
        if application["field_id"] != field_id
    ]

    updated_production_records = [
        record for record in production_records
        if record["field_id"] != field_id
    ]

    save_data(FIELDS_FILE_PATH, updated_fields)
    save_data(APPLICATIONS_FILE_PATH, updated_applications)
    save_data(PRODUCTION_FILE_PATH, updated_production_records)

    oracle_app_success, oracle_app_message = delete_fertilizer_applications_by_field_id(field_id)
    oracle_prod_success, oracle_prod_message = delete_production_records_by_field_id(field_id)
    oracle_field_success, oracle_field_message = delete_field_from_oracle(field_id)

    print(oracle_app_message)
    print(oracle_prod_message)
    print(oracle_field_message)

    write_log(
        "FIELD_DELETED",
        f"Field ID {field_id} deleted - Name: {field_to_delete['name']} | "
        f"Deleted applications: {len(related_applications)} | "
        f"Deleted production records: {len(related_production_records)}"
    )

    print("\nTalhão e registros vinculados excluídos com sucesso!")

def register_fertilizer_application():
    """
    Registers a fertilizer application linked to an existing field.
    """
    print("\n=== REGISTRO DE APLICAÇÃO DE FERTILIZANTE ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado. Cadastre um talhão antes de registrar uma aplicação.")
        return

    print("\nTalhões disponíveis:")
    for field in fields:
        print(f"ID: {field['field_id']} | Nome: {field['name']} | Cultura: {field['crop_type']}")

    field_id = get_valid_field_id(
        "\nDigite o ID do talhão para registrar a aplicação: ",
        fields
    )

    fertilizer_type = get_non_empty_string("Digite o tipo de fertilizante: ")
    quantity = get_positive_float("Digite a quantidade aplicada: ")
    application_date = get_non_empty_string("Digite a data da aplicação (dd/mm/aaaa): ")

    applications = load_data(APPLICATIONS_FILE_PATH)

    application_id = generate_next_id(applications, "application_id")
    new_application = FertilizerApplication(
        application_id,
        field_id,
        fertilizer_type,
        quantity,
        application_date
    )

    applications.append(new_application.to_dict())
    save_data(APPLICATIONS_FILE_PATH, applications)

    oracle_success, oracle_message = insert_fertilizer_application(
        new_application.to_dict()
    )

    print("\nAplicação de fertilizante registrada com sucesso!")
    print(oracle_message)

    write_log(
        "FERTILIZER_APPLICATION_REGISTERED",
        f"Application ID {application_id} registered for Field ID {field_id} | "
        f"Type: {fertilizer_type} | Quantity: {quantity} | Date: {application_date}"
    )

def list_fertilizer_applications():
    """
    Displays all registered fertilizer applications from JSON and Oracle.
    """
    print("\n=== APLICAÇÕES DE FERTILIZANTE EM JSON ===")

    applications = load_data(APPLICATIONS_FILE_PATH)
    fields = load_data(FIELDS_FILE_PATH)

    if not applications:
        print("Nenhuma aplicação de fertilizante cadastrada no JSON.")
    else:
        field_names_by_id = {
            field["field_id"]: field["name"]
            for field in fields
        }

        for application in applications:
            field_name = field_names_by_id.get(
                application["field_id"],
                "Talhão não encontrado"
            )

            print(f"\nID da aplicação: {application['application_id']}")
            print(f"Talhão: {field_name} (ID: {application['field_id']})")
            print(f"Tipo de fertilizante: {application['fertilizer_type']}")
            print(f"Quantidade aplicada: {application['quantity']}")
            print(f"Data da aplicação: {application['application_date']}")

    print("\n=== APLICAÇÕES DE FERTILIZANTE NO ORACLE ===")

    oracle_success, oracle_result = list_fertilizer_applications_from_oracle()

    if not oracle_success:
        print(oracle_result)
        return

    if not oracle_result:
        print("Nenhuma aplicação de fertilizante cadastrada no Oracle.")
        return

    for row in oracle_result:
        print(f"\nID da aplicação: {row[0]}")
        print(f"ID do talhão: {row[1]}")
        print(f"Tipo de fertilizante: {row[2]}")
        print(f"Quantidade aplicada: {row[3]}")
        print(f"Data da aplicação: {row[4]}")

def register_production_record():
    """
    Registers a production record linked to an existing field.
    """
    print("\n=== REGISTRO DE PRODUÇÃO ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado. Cadastre um talhão antes de registrar uma produção.")
        return

    print("\nTalhões disponíveis:")
    for field in fields:
        print(f"ID: {field['field_id']} | Nome: {field['name']} | Cultura: {field['crop_type']}")

    field_id = get_valid_field_id(
        "\nDigite o ID do talhão para registrar a produção: ",
        fields
    )

    harvest_name = get_non_empty_string("Digite o nome da safra ou ciclo produtivo: ")
    production_amount = get_positive_float("Digite a quantidade produzida: ")
    record_date = get_non_empty_string("Digite a data do registro (dd/mm/aaaa): ")

    production_records = load_data(PRODUCTION_FILE_PATH)

    record_id = generate_next_id(production_records, "record_id")
    new_record = ProductionRecord(
        record_id,
        field_id,
        harvest_name,
        production_amount,
        record_date
    )

    production_records.append(new_record.to_dict())
    save_data(PRODUCTION_FILE_PATH, production_records)

    oracle_success, oracle_message = insert_production_record(
        new_record.to_dict()
    )

    print("\nRegistro de produção cadastrado com sucesso!")
    print(oracle_message)

    write_log(
        "PRODUCTION_RECORD_REGISTERED",
        f"Production record ID {record_id} registered for Field ID {field_id} | "
        f"Harvest: {harvest_name} | Amount: {production_amount} | Date: {record_date}"
    )

def list_production_records():
    """
    Displays all registered production records from JSON and Oracle.
    """
    print("\n=== REGISTROS DE PRODUÇÃO EM JSON ===")

    production_records = load_data(PRODUCTION_FILE_PATH)
    fields = load_data(FIELDS_FILE_PATH)

    if not production_records:
        print("Nenhum registro de produção cadastrado no JSON.")
    else:
        field_names_by_id = {
            field["field_id"]: field["name"]
            for field in fields
        }

        for record in production_records:
            field_name = field_names_by_id.get(
                record["field_id"],
                "Talhão não encontrado"
            )

            print(f"\nID do registro: {record['record_id']}")
            print(f"Talhão: {field_name} (ID: {record['field_id']})")
            print(f"Safra/Ciclo: {record['harvest_name']}")
            print(f"Quantidade produzida: {record['production_amount']}")
            print(f"Data do registro: {record['record_date']}")

    print("\n=== REGISTROS DE PRODUÇÃO NO ORACLE ===")

    oracle_success, oracle_result = list_production_records_from_oracle()

    if not oracle_success:
        print(oracle_result)
        return

    if not oracle_result:
        print("Nenhum registro de produção cadastrado no Oracle.")
        return

    for row in oracle_result:
        print(f"\nID do registro: {row[0]}")
        print(f"ID do talhão: {row[1]}")
        print(f"Safra/Ciclo: {row[2]}")
        print(f"Quantidade produzida: {row[3]}")
        print(f"Data do registro: {row[4]}")