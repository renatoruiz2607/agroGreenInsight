# utils/validators.py

def get_valid_option(message, min_option, max_option):
    """
    Validates user menu input.
    Ensures the value is an integer within the allowed range.
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


def get_non_empty_string(message):
    """
    Ensures the user enters a non-empty text.
    """
    while True:
        value = input(message).strip()

        if not value:
            print("Este campo não pode ficar vazio.")
        else:
            return value


def get_positive_float(message):
    """
    Ensures the user enters a positive float number.
    """
    while True:
        try:
            value = float(input(message).replace(",", "."))

            if value <= 0:
                print("Digite um valor numérico maior que zero.")
            else:
                return value

        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def get_confirmation(message):
    """
    Ensures the user enters a valid confirmation (s/n).
    Returns True for 's' and False for 'n'.
    """
    while True:
        value = input(message).strip().lower()

        if value in ["s", "n"]:
            return value == "s"
        else:
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            
def get_valid_field_id(message, fields):
    """
    Ensures the user enters an existing field ID.
    """
    valid_ids = [field["field_id"] for field in fields]

    while True:
        try:
            value = int(input(message))

            if value in valid_ids:
                return value

            print("ID de talhão inválido. Escolha um ID da lista.")

        except ValueError:
            print("Entrada inválida. Digite um número válido.")