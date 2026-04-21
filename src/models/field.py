# models/field.py

class Field:
    """
    Represents an agricultural field.
    """

    def __init__(self, field_id, name, area, crop_type):
        self.field_id = field_id
        self.name = name
        self.area = area
        self.crop_type = crop_type

    def to_dict(self):
        """
        Converts the object to a dictionary.
        """
        return {
            "field_id": self.field_id,
            "name": self.name,
            "area": self.area,
            "crop_type": self.crop_type
        }