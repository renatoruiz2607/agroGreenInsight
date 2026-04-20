# menu.py

from utils.validators import get_valid_option
from services.register_service import (
    register_field,
    list_fields,
    delete_field,
    register_fertilizer_application,
    list_fertilizer_applications
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
        print("7. Analisar eficiência")
        print("8. Gerar recomendação sustentável")
        print("9. Sair")

        option = get_valid_option("Escolha uma opção: ", 1, 9)

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
            print(">> Registro de produção ainda não implementado")
        elif option == 7:
            print(">> Análise de eficiência ainda não implementada")
        elif option == 8:
            print(">> Geração de recomendação ainda não implementada")
        elif option == 9:
            print("Encerrando o sistema...")
            break