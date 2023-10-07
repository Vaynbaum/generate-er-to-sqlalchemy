import os

from src.interface import IBaseTable
from src.const import TABULATION
from src.table.fields.field import SQLAlchemyField


class SQLAlchemyTable(IBaseTable):
    def __init__(self, name: str, field: list[SQLAlchemyField]):
        class_name = "".join([n.capitalize() for n in name.split("_")])
        file_name = name.lower()
        table_name = f"{file_name}s"
        super().__init__(class_name, file_name, table_name, field)

    def __fetch_imports(self) -> str:
        imports = set()
        for field in self._fields:
            imports.update(field.import_names())
        res = ""
        for i in imports:
            res += f"{i}, "
        return res[:-2]

    def __compile_fields(self) -> str:
        res = ""
        for field in self._fields:
            res += f"{TABULATION}{field.generate()}\n"
        return res

    def generate(self) -> str:
        imports = self.__fetch_imports()
        fields = self.__compile_fields()
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, "template.py"), "r") as f:
            template = f.read()
        result = template.format(
            class_name=self._class_name,
            table_name=self._table_name,
            fields=fields,
            imports=imports,
        )

        with open(f"{self._file_name}.py", "w") as f_o:
            f_o.write(result)
