# services/analysis_service.py

from data.json_manager import load_data
from utils.validators import get_valid_field_id
from data.txt_manager import write_log
from utils.formatters import (
    print_title,
    print_subtitle,
    print_separator,
    print_empty_message,
    print_key_value
)

USAGE_LEVELS = ("baixo", "moderado", "alto")
EFFICIENCY_LEVELS = ("baixa", "média", "alta")
RISK_LEVELS = ("baixo", "médio", "alto")

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def classify_fertilizer_usage(total_fertilizer):
    """
    Classifies fertilizer usage intensity.
    """
    if total_fertilizer <= 50:
        return USAGE_LEVELS[0]
    elif total_fertilizer <= 100:
        return USAGE_LEVELS[1]
    else:
        return USAGE_LEVELS[2]

def classify_efficiency(efficiency_index):
    """
    Classifies production efficiency.
    """
    if efficiency_index < 2:
        return EFFICIENCY_LEVELS[0]
    elif efficiency_index < 5:
        return EFFICIENCY_LEVELS[1]
    else:
        return EFFICIENCY_LEVELS[2]

def classify_environmental_risk(usage_level, efficiency_level):
    """
    Classifies environmental risk based on fertilizer usage and productivity efficiency.
    """
    if usage_level == USAGE_LEVELS[2] and efficiency_level == EFFICIENCY_LEVELS[0]:
        return RISK_LEVELS[2]

    if usage_level == USAGE_LEVELS[2] and efficiency_level == EFFICIENCY_LEVELS[2]:
        return RISK_LEVELS[1]

    if usage_level == USAGE_LEVELS[0] and efficiency_level == EFFICIENCY_LEVELS[2]:
        return RISK_LEVELS[0]

    return RISK_LEVELS[1]

def analyze_field_efficiency():
    """
    Analyzes fertilizer usage, production efficiency and environmental risk for a selected field.
    """
    print_title("Análise de Eficiência do Talhão")

    fields = load_data(FIELDS_FILE_PATH)

    if not fields:
        print_empty_message("Nenhum talhão cadastrado.")
        return

    print_subtitle("Talhões disponíveis")
    for field in fields:
        print_separator()
        print_key_value("ID", field["field_id"])
        print_key_value("Nome", field["name"])
        print_key_value("Cultura", field["crop_type"])

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

    print_title("Resultado da Análise")
    print_separator()
    print_key_value("Talhão", selected_field["name"])
    print_key_value("Cultura", selected_field["crop_type"])
    print_key_value("Quantidade de aplicações", application_count)
    print_key_value("Volume total de fertilizante", total_fertilizer)
    print_key_value("Quantidade de registros de produção", production_record_count)
    print_key_value("Produção total registrada", total_production)
    print_key_value("Índice de eficiência produtiva", f"{efficiency_index:.2f}")
    print_key_value("Nível de uso de fertilizante", usage_level)
    print_key_value("Nível de eficiência produtiva", efficiency_level)
    print_key_value("Nível de risco ambiental", environmental_risk)

    write_log(
        "FIELD_ANALYZED",
        f"Field ID {field_id} analyzed | "
        f"Fertilizer usage: {usage_level} | "
        f"Efficiency: {efficiency_level} | "
        f"Environmental risk: {environmental_risk}"
    )