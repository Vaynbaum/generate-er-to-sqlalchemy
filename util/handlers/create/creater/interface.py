from abc import ABC, abstractmethod


class IBaseField(ABC):
    def __init__(
        self, name: str, is_primary_key: bool, is_nullable: bool, is_unique: bool
    ):
        self._name = name
        self._is_primary_key = is_primary_key
        self._is_nullable = is_nullable
        self._is_unique = is_unique

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def import_names(self) -> list[str]:
        raise NotImplementedError()


class IBaseTable(ABC):
    def __init__(self, class_name: str, file_name: str, table_name: str):
        self._class_name = class_name
        self._table_name = table_name
        self._file_name = file_name
        self._fields: list[IBaseField] = []

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError()

    def add_field(self, field: IBaseField):
        self._fields.append(field)

    def delete_field(self, field: IBaseField):
        self._fields.remove(field)
