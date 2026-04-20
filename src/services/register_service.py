# services/register_service.py

from models.field import Field
from models.fertilizer_application import FertilizerApplication
from utils.validators import (
    get_non_empty_string,
    get_positive_float,
    get_confirmation,
    get_valid_field_id
)
from data.json_manager import load_data, save_data

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"

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
    Deletes a field by its ID.
    """
    print("\n=== EXCLUSÃO DE TALHÃO ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado.")
        return

    # Mostrar lista antes de excluir
    for field in fields:
        print(f"\nID: {field['field_id']} - Nome: {field['name']}")

    try:
        field_id = int(input("\nDigite o ID do talhão que deseja excluir: "))
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        return

    # Buscar talhão
    field_to_delete = None
    for field in fields:
        if field["field_id"] == field_id:
            field_to_delete = field
            break

    if not field_to_delete:
        print("Talhão não encontrado.")
        return

    # Confirmação
    confirm = get_confirmation(
    f"Tem certeza que deseja excluir o talhão '{field_to_delete['name']}'? (s/n): "
)
    if not confirm:
        print("Exclusão cancelada.")
        return

    # Remover
    fields.remove(field_to_delete)

    # Reorganizar IDs (boa prática)
    for index, field in enumerate(fields):
        field["field_id"] = index + 1

    save_data(FIELDS_FILE_PATH, fields)

    print("Talhão excluído com sucesso!")

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