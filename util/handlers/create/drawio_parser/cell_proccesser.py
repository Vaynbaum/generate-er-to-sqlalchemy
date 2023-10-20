from handlers.create.drawio_parser.const import *
from handlers.create.drawio_parser.field_proccesser import (
    DrawERFieldProccesser,
)
from handlers.create.interface import TableFromDiagramSchema
from handlers.create.utils import camel_to_snake


class DrawERCellProccesser:
    def __init__(self):
        self.__field_proccesser = DrawERFieldProccesser()

    def proccess(self, cells: dict):
        tables = {}
        for k, cell in cells.items():
            if cell["type"] == TABLE:
                name: str = cell["data"]["value"]

                tablename = camel_to_snake(name)
                t = tablename
                if name[IND_LONG_WORD_END:] == LONG_WORD_END:
                    name = f"{name[:IND_LONG_WORD_END]}{SHORT_WORD_END}"
                    t = f"{t[:IND_LONG_WORD_END]}{SHORT_WORD_END}"
                class_name = name[:IND_SHORT_WORD_END]
                file_name = f"{t[:IND_SHORT_WORD_END]}.{PY_FILE_EXTENSION}"

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
