# models/fertilizer_application.py

class FertilizerApplication:
    """
    Represents a fertilizer application linked to a field.
    """

    def __init__(self, application_id, field_id, fertilizer_type, quantity, application_date):
        self.application_id = application_id
        self.field_id = field_id
        self.fertilizer_type = fertilizer_type
        self.quantity = quantity
        self.application_date = application_date

    def to_dict(self):
        """
        Converts the object to a dictionary.
        """
        return {
            "application_id": self.application_id,
            "field_id": self.field_id,
            "fertilizer_type": self.fertilizer_type,
            "quantity": self.quantity,
            "application_date": self.application_date
        }