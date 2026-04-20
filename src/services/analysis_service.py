# services/analysis_service.py

from data.json_manager import load_data
from utils.validators import get_valid_field_id
from data.txt_manager import write_log

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def classify_fertilizer_usage(total_fertilizer):
    """
    Classifies fertilizer usage intensity.
    """
    if total_fertilizer <= 50:
        return "baixo"
    if total_fertilizer <= 100:
        return "moderado"
    return "alto"

def classify_efficiency(efficiency_index):
    """
    Classifies production efficiency.
    """
    if efficiency_index < 2:
        return "baixa"
    if efficiency_index <= 4:
        return "média"
    return "alta"

def classify_environmental_risk(usage_level, efficiency_level):
    """
    Classifies environmental risk based on fertilizer usage and productivity efficiency.
    """
    if usage_level == "alto" and efficiency_level == "baixa":
        return "alto"

    if usage_level == "moderado" and efficiency_level == "baixa":
        return "médio"

    if usage_level == "alto" and efficiency_level == "média":
        return "médio"

    if usage_level == "baixo" and efficiency_level == "alta":
        return "baixo"

    return "médio"

def analyze_field_efficiency():
    """
    Analyzes fertilizer usage, production efficiency and environmental risk for a selected field.
    """
    print("\n=== ANÁLISE DE EFICIÊNCIA DO TALHÃO ===")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print("Nenhum talhão cadastrado.")
        return

    print("\nTalhões disponíveis:")
    for field in fields:
        print(f"ID: {field['field_id']} | Nome: {field['name']} | Cultura: {field['crop_type']}")

    field_id = get_valid_field_id(
        "\nDigite o ID do talhão para análise: ",
        fields
    )

    selected_field = next(
        (field for field in fields if field["field_id"] == field_id),
        None
    )

    applications = load_data(APPLICATIONS_FILE_PATH)
    production_records = load_data(PRODUCTION_FILE_PATH)

    field_applications = [
        application for application in applications
        if application["field_id"] == field_id
    ]

    field_production_records = [
        record for record in production_records
        if record["field_id"] == field_id
    ]

    total_fertilizer = sum(
        application["quantity"]
        for application in field_applications
    )

    total_production = sum(
        record["production_amount"]
        for record in field_production_records
    )

    application_count = len(field_applications)
    production_record_count = len(field_production_records)

    efficiency_index = (
        total_production / total_fertilizer
        if total_fertilizer > 0 else 0
    )

    usage_level = classify_fertilizer_usage(total_fertilizer)
    efficiency_level = classify_efficiency(efficiency_index)
    environmental_risk = classify_environmental_risk(
        usage_level,
        efficiency_level
    )

    print("\n=== RESULTADO DA ANÁLISE ===")
    print(f"Talhão: {selected_field['name']}")
    print(f"Cultura: {selected_field['crop_type']}")
    print(f"Quantidade de aplicações: {application_count}")
    print(f"Volume total de fertilizante: {total_fertilizer}")
    print(f"Quantidade de registros de produção: {production_record_count}")
    print(f"Produção total registrada: {total_production}")
    print(f"Índice de eficiência produtiva: {efficiency_index:.2f}")
    print(f"Nível de uso de fertilizante: {usage_level}")
    print(f"Nível de eficiência produtiva: {efficiency_level}")
    print(f"Nível de risco ambiental: {environmental_risk}")

    write_log(
        "FIELD_ANALYZED",
        f"Field ID {field_id} analyzed | "
        f"Fertilizer usage: {usage_level} | "
        f"Efficiency: {efficiency_level} | "
        f"Environmental risk: {environmental_risk}"
    )