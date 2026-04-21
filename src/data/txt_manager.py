# data/txt_manager.py

from datetime import datetime

LOG_FILE_PATH = "src/data/system_log.txt"

def write_log(action, details):
    """
    Writes a log entry to the TXT file.
    """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_message = f"[{timestamp}] {action}: {details}\n"

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
        file.write(log_message)