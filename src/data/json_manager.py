# data/json_manager.py

import json
import os

def load_data(file_path):
    """
    Loads data from a JSON file.
    Returns an empty list if the file does not exist or is empty.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(file_path, data):
    """
    Saves data to a JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)