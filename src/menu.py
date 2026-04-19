# menu.py

from utils.validators import get_valid_option

def main_menu():
    while True:
        print("\n=== AGROGREEN INSIGHT ===")
        print("1. Cadastrar talhão")
        print("2. Registrar aplicação de fertilizante")
        print("3. Registrar produção")
        print("4. Analisar eficiência")
        print("5. Gerar recomendação sustentável")
        print("6. Sair")

        option = get_valid_option("Escolha uma opção: ", 1, 6)

        if option == 1:
            print(">> Cadastro de talhão ainda não implementado")
        elif option == 2:
            print(">> Registro de aplicação ainda não implementado")
        elif option == 3:
            print(">> Registro de produção ainda não implementado")
        elif option == 4:
            print(">> Análise de eficiência ainda não implementada")
        elif option == 5:
            print(">> Geração de recomendação ainda não implementada")
        elif option == 6:
            print("Encerrando o sistema...")
            break