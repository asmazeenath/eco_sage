# utils/validators.py

import json


REQUIRED_FIELDS = {
    "soil": [
        "ph",
        "organic_matter",
        "soil_moisture"
    ],
    "climate": [
        "temperature",
        "rainfall"
    ],
    "land": [
        "land_use"
    ]
}


def validate_environment_data(data):
    """
    Validate environmental input and return missing fields.
    """

    missing = []

    soil = data.get("soil", {})
    climate = data.get("climate", {})
    land = data.get("land", {})

    for field in REQUIRED_FIELDS["soil"]:
        if soil.get(field) in [None, "", "unknown"]:
            missing.append(field)

    for field in REQUIRED_FIELDS["climate"]:
        if climate.get(field) in [None, "", "unknown"]:
            missing.append(field)

    if land.get("land_use") in [None, "", "unknown"]:
        missing.append("land_use")

    return missing


def parse_json_input(text):
    """
    Convert JSON text into Python dictionary.
    """

    try:
        data = json.loads(text)
        return data, None

    except json.JSONDecodeError as e:
        return None, f"Invalid JSON: {e}"


def safe_float(value):

    try:
        return float(value)

    except (ValueError, TypeError):
        return None