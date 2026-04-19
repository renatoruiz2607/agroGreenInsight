# menu.py

from utils.validators import get_valid_option
from services.register_service import register_field, list_fields, delete_field

def main_menu():
    while True:
        print("\n=== AGROGREEN INSIGHT ===")
        print("1. Cadastrar talhão")
        print("2. Listar talhões")
        print("3. Excluir talhão")
        print("4. Registrar aplicação de fertilizante")
        print("5. Registrar produção")
        print("6. Analisar eficiência")
        print("7. Gerar recomendação sustentável")
        print("8. Sair")

        option = get_valid_option("Escolha uma opção: ", 1, 8)

        if option == 1:
            register_field()
        elif option == 2:
            list_fields()
        elif option == 3:
            delete_field()
        elif option == 4:
            print(">> Registro de aplicação ainda não implementado")
        elif option == 5:
            print(">> Registro de produção ainda não implementado")
        elif option == 6:
            print(">> Análise de eficiência ainda não implementada")
        elif option == 7:
            print(">> Geração de recomendação ainda não implementada")
        elif option == 8:
            print("Encerrando o sistema...")
            break