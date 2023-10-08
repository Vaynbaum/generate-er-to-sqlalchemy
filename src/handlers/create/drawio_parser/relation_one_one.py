from src.handlers.create.drawio_parser.const import *
from src.handlers.create.drawio_parser.interface import IRelation
from src.handlers.create.interface import TableFromDiagramSchema
from src.handlers.create.utils import field_id_from_tablename


class RepationOneToOne(IRelation):
    def __find_dependent_table(
        self, table_source: TableFromDiagramSchema, table_target: TableFromDiagramSchema
    ):
        for field in table_source.fields:
            if field.is_fk and field.name == field_id_from_tablename(
                table_target.tablename
            ):
                field.fk_table = table_target
                return

        for field in table_target.fields:
            if field.is_fk and field.name == field_id_from_tablename(
                table_source.tablename
            ):
                field.fk_table = table_source
                return

    def handle(self, cell: dict, one: int, _: int, tables: dict):
        if one == 2:
            data = cell["data"]
            field_source = data[SOURCE]
            field_target = data[TARGET]
            table_source = tables[field_source]
            table_target = tables[field_target]
            self.__find_dependent_table(table_source, table_target)
        return tables
