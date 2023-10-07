from src.handlers.create_model.interface import IModelCreater, TableFromDiagramSchema


class DrawERParser(IModelCreater):
    def handle(self, tables: list[TableFromDiagramSchema]):
        ...
