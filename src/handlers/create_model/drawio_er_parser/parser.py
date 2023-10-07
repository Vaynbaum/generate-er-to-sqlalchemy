from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

from src.handlers.create_model.drawio_er_parser.const import *
from src.handlers.create_model.drawio_er_parser import *
from src.handlers.create_model.interface import *


class DrawERParser(IDiagramParser):
    def __init__(self):
        relations = [RepationManyToMany(), RepationOneToMany(), RepationOneToOne()]
        self.__arrow_proccesser = DrawERArrowProccesser(relations)
        self.__cell_proccesser = DrawERCellProccesser()

    def __find_diagram_by_name(self, mxfile: Element, name: str):
        for diagram in mxfile.iter("diagram"):
            if diagram.attrib["name"] == name:
                return diagram
        return None

    def __proccess_ids(self, name_id: str, cell: dict, cells: dict, field_ids: dict):
        if not cell["data"][name_id] in cells:
            id = cell["data"][name_id]
            cell["data"][name_id] = field_ids[id]["parent"]

    def __parse_data_from_diagram(self, diagram: Element):
        cells = {}
        field_ids = {}

        if diagram:
            for cell in diagram.iter("mxCell"):
                id = cell.attrib["id"]
                parent_id = cell.attrib.get("parent", None)

                if parent_id and parent_id == "1":
                    type = None
                    for k, v in TYPES.items():
                        if k in cell.attrib["style"]:
                            type = v
                            break
                    cells[id] = {"data": cell.attrib, "type": type, "cells": []}
                elif parent_id and parent_id in cells:
                    arr = cells[parent_id]["cells"]
                    arr.append({"data": cell.attrib, "dependent": None})
                    field_ids[id] = {"parent": parent_id, "ind": len(arr) - 1}
                elif parent_id and parent_id in field_ids:
                    data = field_ids[parent_id]
                    arr = cells[data["parent"]]["cells"]
                    field = arr[data["ind"]]
                    field["dependent"] = cell.attrib

            for cell in cells.values():
                if cell["type"] == ARROW:
                    self.__proccess_ids(SOURCE, cell, cells, field_ids)
                    self.__proccess_ids(TARGET, cell, cells, field_ids)
        return cells

    def handle(self, config: ParserConfig):
        tree = ET.parse(config.file_path)
        mxfile = tree.getroot()
        diagram = self.__find_diagram_by_name(mxfile, config.name_page)
        cells = self.__parse_data_from_diagram(diagram)
        tables = self.__cell_proccesser.proccess(cells)
        tables = self.__arrow_proccesser.proccess(cells, tables)
        return [table for table in tables.values()]
