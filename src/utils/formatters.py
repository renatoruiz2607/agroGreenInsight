# utils/formatters.py

def print_title(title):
    print(f"\n=== {title.upper()} ===")

def print_subtitle(subtitle):
    print(f"\n--- {subtitle} ---")

def print_separator():
    print("-" * 40)

def print_empty_message(message):
    print(f"\n{message}")

def print_key_value(label, value):
    print(f"{label}: {value}")