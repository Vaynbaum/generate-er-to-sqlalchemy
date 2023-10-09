import re
from src.handlers.create.interface import FieldDiagramSchema
from src.handlers.create.utils import clear_str_from_tag


class DrawERFieldProccesser:
    def proccess(self, field: dict):
        value = field["data"]["value"]
        value = clear_str_from_tag(value)
        value = re.sub(r'[, :]', " ", value)
        values = value.split(" ")
        name_field = values[0]
        type_field = "varchar"
        default = None
        if len(values) > 1:
            type_field = values[1]
        if len(values) > 2:
            default = values[2]

        is_primary = False
        is_fk = False
        dependent = field["dependent"]
        if dependent:
            value = dependent["value"]
            value = clear_str_from_tag(value).lower()
            is_primary = "pk" in value
            is_fk = "fk" in value
            is_not_null = "n" in value
            is_unique = "u" in value
        return FieldDiagramSchema(
            id=field["data"]["id"],
            name=name_field,
            type=type_field,
            is_primary=is_primary,
            is_fk=is_fk,
            default=default,
            is_not_null=is_not_null,
            is_unique=is_unique,
        )
