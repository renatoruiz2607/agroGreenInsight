# services/recommendation_service.py

from data.json_manager import load_data
from utils.validators import get_valid_field_id
from services.analysis_service import (
    classify_fertilizer_usage,
    classify_efficiency,
    classify_environmental_risk,
    USAGE_LEVELS,
    EFFICIENCY_LEVELS,
    RISK_LEVELS
)
from data.txt_manager import write_log
from utils.formatters import (
    print_title,
    print_subtitle,
    print_separator,
    print_empty_message,
    print_key_value
)

FIELDS_FILE_PATH = "src/data/fields.json"
APPLICATIONS_FILE_PATH = "src/data/fertilizer_applications.json"
PRODUCTION_FILE_PATH = "src/data/production_records.json"

def generate_recommendation_message(usage_level, efficiency_level, environmental_risk):
    """
    Generates a sustainable recommendation based on fertilizer usage,
    productivity efficiency and environmental risk.
    """
    if (
        usage_level == USAGE_LEVELS[0]
        and efficiency_level == EFFICIENCY_LEVELS[2]
        and environmental_risk == RISK_LEVELS[0]
    ):
        return (
            "Manter a estratégia atual, pois o talhão apresenta bom retorno produtivo "
            "com baixo impacto ambiental."
        )

    if (
        usage_level == USAGE_LEVELS[2]
        and efficiency_level == EFFICIENCY_LEVELS[0]
        and environmental_risk == RISK_LEVELS[2]
    ):
        return (
            "Reduzir a intensidade de aplicação e revisar o manejo do talhão, "
            "pois há alto consumo de insumos, baixo retorno produtivo e elevado risco ambiental."
        )

    if (
        usage_level == USAGE_LEVELS[2]
        and efficiency_level == EFFICIENCY_LEVELS[2]
        and environmental_risk == RISK_LEVELS[1]
    ):
        return (
            "Manter o bom desempenho produtivo, mas avaliar alternativas para reduzir a "
            "dependência de fertilizantes e aumentar a sustentabilidade da operação."
        )

    if (
        usage_level == USAGE_LEVELS[0]
        and efficiency_level == EFFICIENCY_LEVELS[0]
        and environmental_risk == RISK_LEVELS[1]
    ):
        return (
            "Revisar o planejamento produtivo do talhão, pois o baixo uso de fertilizante "
            "não está resultando em bom desempenho produtivo."
        )

    return (
        "Monitorar o desempenho do talhão e ajustar gradualmente a estratégia de aplicação, "
        "buscando maior equilíbrio entre produtividade e impacto ambiental."
    )

def generate_sustainable_recommendation():
    """
    Generates a sustainable recommendation for a selected field.
    """
    print_title("Recomendação Sustentável")

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
        "\nDigite o ID do talhão para gerar a recomendação: ",
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

    recommendation = generate_recommendation_message(
        usage_level,
        efficiency_level,
        environmental_risk
    )

    print_title("Resultado da Recomendação")
    print_separator()

    print_key_value("Talhão", selected_field["name"])
    print_key_value("Cultura", selected_field["crop_type"])
    print_key_value("Nível de uso de fertilizante", usage_level)
    print_key_value("Nível de eficiência produtiva", efficiency_level)
    print_key_value("Nível de risco ambiental", environmental_risk)

    print_subtitle("Recomendação")
    print(recommendation)

    write_log(
        "SUSTAINABLE_RECOMMENDATION_GENERATED",
        f"Field ID {field_id} recommendation generated | "
        f"Usage: {usage_level} | "
        f"Efficiency: {efficiency_level} | "
        f"Risk: {environmental_risk}"
    )