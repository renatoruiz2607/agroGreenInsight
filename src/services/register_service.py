# services/register_service.py

from models.field import Field
from utils.validators import get_non_empty_string, get_positive_float, get_confirmation
from data.json_manager import load_data, save_data

FIELDS_FILE_PATH = "src/data/fields.json"

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