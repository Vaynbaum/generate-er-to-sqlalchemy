from src.handlers.create_model.drawio_er_parser.const import TABLE
from src.handlers.create_model.drawio_er_parser.field_proccesser import (
    DrawERFieldProccesser,
)
from src.handlers.create_model.interface import TableFromDiagramSchema
from src.handlers.create_model.utils import camel_to_snake


class DrawERCellProccesser:
    def __init__(self):
        self.__field_proccesser = DrawERFieldProccesser()

    def proccess(self, cells: dict):
        tables = {}
        for k, cell in cells.items():
            if cell["type"] == TABLE:
                name: str = cell["data"]["value"]
                class_name = name[:-1]
                tablename = camel_to_snake(name)
                file_name = f"{class_name.lower()}.py"
                fields = []
                for field in cell["cells"]:
                    if "value" in field["data"]:
                        fields.append(self.__field_proccesser.proccess(field))
                tables[k] = TableFromDiagramSchema(
                    class_name=class_name,
                    tablename=tablename,
                    file_name=file_name,
                    fields=fields,
                )
        return tables
