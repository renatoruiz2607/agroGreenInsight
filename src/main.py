# main.py

from menu import main_menu
from data.oracle_manager import initialize_oracle_database

def main():
    """
    Entry point of the application.
    Initializes Oracle database structure and starts the menu.
    """
    success, messages = initialize_oracle_database()

    print("\n=== INICIALIZAÇÃO DO SISTEMA ===")
    for message in messages:
        print(message)

    main_menu()

if __name__ == "__main__":
    main()