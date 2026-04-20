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

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def register_field():
    """
    Registers a new field and saves it to a JSON file.
    """
    print("\n=== CADASTRO DE TALHÃO ===")

    name = get_non_empty_string("Digite o nome do talhão: ")
    area = get_positive_float("Digite a área do talhão em hectares: ")
    crop_type = get_non_empty_string("Digite a cultura plantada: ")

    fields = load_data(FIELDS_FILE_PATH)

    field_id = len(fields) + 1
    new_field = Field(field_id, name, area, crop_type)

    fields.append(new_field.to_dict())
    save_data(FIELDS_FILE_PATH, fields)

    print("\nTalhão cadastrado com sucesso!")

def list_fields():
    """
    Displays all registered fields.
    """
    print("\n=== LISTA DE TALHÕES ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado.")
        return

    for field in fields:
        print(f"\nID: {field['field_id']}")
        print(f"Nome: {field['name']}")
        print(f"Área (ha): {field['area']}")
        print(f"Cultura: {field['crop_type']}")

def delete_field():
    """
    Deletes a field and all related fertilizer applications and production records.
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

    for index, field in enumerate(updated_fields):
        old_field_id = field["field_id"]
        new_field_id = index + 1
        field["field_id"] = new_field_id

        for application in updated_applications:
            if application["field_id"] == old_field_id:
                application["field_id"] = new_field_id

        for record in updated_production_records:
            if record["field_id"] == old_field_id:
                record["field_id"] = new_field_id

    for index, application in enumerate(updated_applications):
        application["application_id"] = index + 1

    for index, record in enumerate(updated_production_records):
        record["record_id"] = index + 1

    save_data(FIELDS_FILE_PATH, updated_fields)
    save_data(APPLICATIONS_FILE_PATH, updated_applications)
    save_data(PRODUCTION_FILE_PATH, updated_production_records)

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

    application_id = len(applications) + 1
    new_application = FertilizerApplication(
        application_id,
        field_id,
        fertilizer_type,
        quantity,
        application_date
    )

    applications.append(new_application.to_dict())
    save_data(APPLICATIONS_FILE_PATH, applications)

    print("\nAplicação de fertilizante registrada com sucesso!")

def list_fertilizer_applications():
    """
    Displays all registered fertilizer applications.
    """
    print("\n=== LISTA DE APLICAÇÕES DE FERTILIZANTE ===")

    applications = load_data(APPLICATIONS_FILE_PATH)
    fields = load_data(FIELDS_FILE_PATH)

    if not applications:
        print("Nenhuma aplicação de fertilizante cadastrada.")
        return

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

    record_id = len(production_records) + 1
    new_record = ProductionRecord(
        record_id,
        field_id,
        harvest_name,
        production_amount,
        record_date
    )

    production_records.append(new_record.to_dict())
    save_data(PRODUCTION_FILE_PATH, production_records)

    print("\nRegistro de produção cadastrado com sucesso!")

def list_production_records():
    """
    Displays all registered production records.
    """
    print("\n=== LISTA DE REGISTROS DE PRODUÇÃO ===")

    production_records = load_data(PRODUCTION_FILE_PATH)
    fields = load_data(FIELDS_FILE_PATH)

    if not production_records:
        print("Nenhum registro de produção cadastrado.")
        return

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