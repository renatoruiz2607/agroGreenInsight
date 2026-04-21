# models/production_record.py

class ProductionRecord:
    """
    Represents a production record linked to a field.
    """

    def __init__(self, record_id, field_id, harvest_name, production_amount, record_date):
        self.record_id = record_id
        self.field_id = field_id
        self.harvest_name = harvest_name
        self.production_amount = production_amount
        self.record_date = record_date

    def to_dict(self):
        """
        Converts the object to a dictionary.
        """
        return {
            "record_id": self.record_id,
            "field_id": self.field_id,
            "harvest_name": self.harvest_name,
            "production_amount": self.production_amount,
            "record_date": self.record_date
        }