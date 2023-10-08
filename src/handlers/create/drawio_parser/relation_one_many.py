from src.handlers.create.drawio_parser.const import ASSOCIATIONS
from src.handlers.create.drawio_parser.interface import IRelation
from src.handlers.create.utils import field_id_from_tablename


class RepationOneToMany(IRelation):
    def handle(self, cell: dict, one: int, many: int, tables: dict):
        if one and many:
            data = cell["data"]
            styles = data["style"].split(";")
            for style in styles:
                if "ER" in style:
                    style = style.lower()
                    if "many" in style:
                        many = style.split("=")[0]
                    elif "one" in style:
                        one = style.split("=")[0]
            field_many = ASSOCIATIONS[many]
            field_one = ASSOCIATIONS[one]
            table_many = tables[data[field_many]]
            table_one = tables[data[field_one]]
            for field in table_many.fields:
                if field.name == field_id_from_tablename(table_one.tablename):
                    field.fk_table = table_one
        return tables
