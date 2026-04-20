# menu.py

from utils.validators import get_valid_option
from services.register_service import (
    register_field,
    list_fields,
    delete_field,
    register_fertilizer_application,
    list_fertilizer_applications,
    register_production_record,
    list_production_records
)

def main_menu():
    while True:
        print("\n=== AGROGREEN INSIGHT ===")
        print("1. Cadastrar talhão")
        print("2. Listar talhões")
        print("3. Excluir talhão")
        print("4. Registrar aplicação de fertilizante")
        print("5. Listar aplicações de fertilizante")
        print("6. Registrar produção")
        print("7. Listar produção")
        print("8. Analisar eficiência")
        print("9. Gerar recomendação sustentável")
        print("10. Sair")

        option = get_valid_option("Escolha uma opção: ", 1, 10)

        if option == 1:
            register_field()
        elif option == 2:
            list_fields()
        elif option == 3:
            delete_field()
        elif option == 4:
            register_fertilizer_application()
        elif option == 5:
            list_fertilizer_applications()
        elif option == 6:
            register_production_record()
        elif option == 7:
            list_production_records()
        elif option == 8:
            print(">> Análise de eficiência ainda não implementada")
        elif option == 9:
            print(">> Geração de recomendação ainda não implementada")
        elif option == 10:
            print("Encerrando o sistema...")
            break