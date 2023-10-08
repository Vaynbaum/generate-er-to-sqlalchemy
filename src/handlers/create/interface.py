from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel


class ParserConfig(BaseModel):
    file_path: str | None = ""
    name_page: str | None = ""


class TableFromDiagramSchema(BaseModel):
    class_name: str
    tablename: str
    file_name: str
    fields: List["FieldDiagramSchema"] = []


class FieldDiagramSchema(BaseModel):
    name: str
    type: str
    is_primary: bool = False
    is_fk: bool = False
    fk_table: TableFromDiagramSchema | None = None


class IDiagramParser(ABC):
    @abstractmethod
    def handle(self, config: ParserConfig):
        raise NotImplementedError()


class IModelCreater(ABC):
    @abstractmethod
    def handle(self, tables: list[TableFromDiagramSchema], path_ini_file: str):
        raise NotImplementedError()
