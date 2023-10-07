from abc import ABC, abstractmethod

from src.interface import IBaseField


class BaseNote(ABC):
    @abstractmethod
    def generate(self, kwargs):
        raise NotImplementedError()


class PrimaryNote(BaseNote):
    def generate(self, flag: bool):
        return f", primary_key={flag}" if flag else ""


class UniqueNote(BaseNote):
    def generate(self, flag: bool):
        return f", unique={flag}"


class NullableNote(BaseNote):
    def generate(self, flag: bool):
        return f", nullable={flag}" if flag else ""


class SQLAlchemyField(IBaseField, ABC):
    def __init__(
        self, name: str, is_primary_key: bool, is_nullable: bool, is_unique: bool
    ):
        super().__init__(name, is_primary_key, is_nullable, is_unique)
        self.__primary_note = PrimaryNote()
        self.__unique_note = UniqueNote()
        self.__nullable_note = NullableNote()
        self.__column = "Column"

    def generate(self) -> str:
        notes = "".join(
            [
                self.__primary_note.generate(self._is_primary_key),
                self.__unique_note.generate(self._is_unique),
                self.__nullable_note.generate(self._is_nullable),
            ]
        )
        return "".join([f"{self._name} = {self.__column}", "({type_field}", notes, ")"])

    def import_names(self) -> list[str]:
        return [self.__column]
