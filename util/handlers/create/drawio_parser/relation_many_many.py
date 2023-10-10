from handlers.create.drawio_parser.const import *
from handlers.create.drawio_parser.interface import IRelation
from handlers.create.interface import (
    FieldDiagramSchema,
    TableFromDiagramSchema,
)
from handlers.create.utils import camel_to_snake, field_id_from_tablename


class RepationManyToMany(IRelation):
    def __create_field_id(self, table: TableFromDiagramSchema):
        name = field_id_from_tablename(table.tablename)
        field = FieldDiagramSchema(
            name=name, is_primary=True, is_fk=True, type="integer", fk_table=table
        )
        return field

    def __create_link(
        self, table_source: TableFromDiagramSchema, table_target: TableFromDiagramSchema
    ):
        class_name = f"{table_source.class_name}{table_target.class_name}Link"
        tablename = f"{camel_to_snake(class_name)}s"
        file_name = f"{tablename[:-1]}.py"
        fields = [
            self.__create_field_id(table_source),
            self.__create_field_id(table_target),
        ]
        table = TableFromDiagramSchema(
            class_name=class_name,
            tablename=tablename,
            file_name=file_name,
            fields=fields,
        )
        return table

    def handle(self, cell: dict, _: int, many: int, tables: dict):
        if many == 2:
            data = cell["data"]
            field_source = data[SOURCE]
            field_target = data[TARGET]
            table_source = tables[field_source]
            table_target = tables[field_target]
            table = self.__create_link(table_source, table_target)
            tables[f"synthetic_{table.tablename}"] = table
        return tables
