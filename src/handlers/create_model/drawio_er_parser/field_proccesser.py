from src.handlers.create_model.interface import FieldDiagramSchema
from src.handlers.create_model.utils import clear_str_from_tag


class DrawERFieldProccesser:
    def proccess(self, field: dict):
        value = field["data"]["value"]
        value = clear_str_from_tag(value)
        values = value.split(":")
        name_field = values[0]
        type_field = "varchar"
        if len(values) > 1:
            type_field = values[1]

        is_primary = False
        is_fk = False
        dependent = field["dependent"]
        if dependent:
            value = dependent["value"]
            value = clear_str_from_tag(value).lower()
            is_primary = "pk" in value
            is_fk = "fk" in value
        return FieldDiagramSchema(
            name=name_field, type=type_field, is_primary=is_primary, is_fk=is_fk
        )
