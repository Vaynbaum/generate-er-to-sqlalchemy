from src.fields.field import IBaseField, SQLAlchemyField


class IntegerField(IBaseField):
    def __init__(
        self, name: str, is_primary_key: bool, is_nullable: bool, is_unique: bool
    ):
        super().__init__(name, is_primary_key, is_nullable, is_unique)


class IntegerSQLAlchemyField(SQLAlchemyField):
    def __init__(
        self,
        name: str,
        is_primary_key: bool = False,
        is_nullable: bool = True,
        is_unique: bool = False,
    ):
        super().__init__(name, is_primary_key, is_nullable, is_unique)
        self.__type_field = "Integer"

    def generate(self) -> str:
        common_str = super().generate()
        return common_str.format(type_field=self.__type_field)

    def import_names(self) -> str:
        imports = super().import_names()
        imports.append(self.__type_field)
        return imports
