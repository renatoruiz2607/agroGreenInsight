# utils/helpers.py

def generate_next_id(records, id_field):
    """
    Generates the next integer ID based on the highest existing ID.
    """
    return max((record[id_field] for record in records), default=0) + 1