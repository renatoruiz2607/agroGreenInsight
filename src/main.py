# main.py

from menu import main_menu
from data.oracle_manager import (
    initialize_oracle_database,
    sync_json_data_to_oracle
)
from data.json_manager import load_data

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def main():
    """
    Entry point of the application.
    Initializes Oracle database structure, synchronizes JSON data to Oracle,
    and starts the menu.
    """
    success, messages = initialize_oracle_database()

    print("\n=== INICIALIZAÇÃO DO SISTEMA ===")
    for message in messages:
        print(message)

    fields = load_data(FIELDS_FILE_PATH)
    applications = load_data(APPLICATIONS_FILE_PATH)
    production_records = load_data(PRODUCTION_FILE_PATH)

    sync_result = sync_json_data_to_oracle(
        fields,
        applications,
        production_records
    )

    print("\n=== SINCRONIZAÇÃO JSON -> ORACLE ===")
    print(f"Talhões inseridos no Oracle: {sync_result['fields_inserted']}")
    print(f"Aplicações inseridas no Oracle: {sync_result['applications_inserted']}")
    print(f"Produções inseridas no Oracle: {sync_result['production_inserted']}")

    main_menu()

if __name__ == "__main__":
    main()