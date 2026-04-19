# utils/validators.py

def get_valid_option(message, min_option, max_option):
    """
    Validates user menu input
    Ensures the value is an integer within the allowed range
    """
    while True:
        try:
            value = int(input(message))

            if value < min_option or value > max_option:
                print(f"Por favor, insira um número entre {min_option} e {max_option}.")
            else:
                return value

        except ValueError:
            print("Entrada inválida. Digite um número válido.")