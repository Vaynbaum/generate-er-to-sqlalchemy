from src.fields.field import IBaseField, SQLAlchemyField


class StringField(IBaseField):
    def __init__(
        self,
        name: str,
        is_primary_key: bool,
        is_nullable: bool,
        is_unique: bool,
        max_length: int | None = None,
    ):
        super().__init__(name, is_primary_key, is_nullable, is_unique)
        self._max_length = max_length


class StringSQLAlchemyField(SQLAlchemyField):
    def __init__(
        self,
        name: str,
        max_length: int | None = None,
        is_primary_key: bool = False,
        is_nullable: bool = True,
        is_unique: bool = False,
    ):
        super().__init__(name, is_primary_key, is_nullable, is_unique)
        self.__max_length = max_length
        self.__type_field = "String"

    def generate(self) -> str:
        common_str = super().generate()
        max_len = self.__max_length if self.__max_length else ""
        return common_str.format(type_field=f"{self.__type_field}({max_len})")

    def import_names(self) -> str:
        imports = super().import_names()
        imports.append(self.__type_field)
        return imports
