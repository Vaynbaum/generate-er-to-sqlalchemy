from abc import ABC, abstractmethod


class IRelation(ABC):
    @abstractmethod
    def handle(self, cell: dict, one: int, many: int, tables: dict):
        raise NotImplementedError()
