import os

from src.const import *
from src.handlers.create.interface import IModelCreater, TableFromDiagramSchema
from src.handlers.create.utils import ini_file_to_dict


class SQLAlchemyModelCreater(IModelCreater):
    def handle(self, tables: list[TableFromDiagramSchema], path_ini_file: str):
        with open(path_ini_file, "r", encoding="utf8") as file:
            ini_data = file.read()
            ini_data = ini_file_to_dict(ini_data)

        for table in tables:
            self.__create_table(table, ini_data)

    def __create_table(self, table: TableFromDiagramSchema, ini_data: dict):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, "template.py"), "r") as f:
            template = f.read()
        with open(os.path.join(ini_data[KW_APP], ini_data[KW_AUTO], table.file_name), "w") as model_file:
            model_content = template
            model_file.write(model_content)
