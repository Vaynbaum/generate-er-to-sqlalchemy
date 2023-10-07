from src.handlers.create_model.drawio_er_parser.const import *
from src.handlers.create_model.drawio_er_parser.interface import IRelation


class DrawERArrowProccesser:
    def __init__(self, relations: list[IRelation]):
        self.__relations = relations

    def proccess(self, cells: dict, tables: dict):
        for cell in cells.values():
            if cell["type"] == ARROW:
                data = cell["data"]
                styles = data["style"].split(";")
                one = 0
                many = 0
                for style in styles:
                    if "ER" in style:
                        style = style.lower()
                        if "many" in style:
                            many += 1
                        elif "one" in style:
                            one += 1
                for relation in self.__relations:
                    relation.handle(cell, one, many, tables)
        return tables
