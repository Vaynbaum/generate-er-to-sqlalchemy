# from src.fields.integer_field import IntegerSQLAlchemyField
# from src.fields.string_field import StringSQLAlchemyField
# from src.table import SQLAlchemyTable

# # fields = [
# #     IntegerSQLAlchemyField("id", is_primary_key=True),
# #     StringSQLAlchemyField("name", 255, is_unique=True),
# # ]
# # table = SQLAlchemyTable("tag", fields)

# fields = [
#     IntegerSQLAlchemyField("id", is_primary_key=True),
#     StringSQLAlchemyField("img", is_nullable=False),
#     StringSQLAlchemyField("note", is_nullable=False),
#     IntegerSQLAlchemyField("hotel_id"),
# ]
# table = SQLAlchemyTable("hotel_image", fields)
# table.generate()

import argparse

from src.const import *
from src.factory import create_main_controller


controller = create_main_controller()
parser = argparse.ArgumentParser(description="Описание программы")
parser.add_argument("action", choices=ACTIONS, help="Выбрать действие программы")
name_help = "Название проекта, по умолчанию 'app'"
parser.add_argument("-n", "--name", type=str, help=name_help)
parser.add_argument("-e", "--er_file", type=str, help="Файл drawio с ER диаграммой")
parser.add_argument("-p", "--page_name", type=str, help="Файл drawio с ER диаграммой")
parser.add_argument(
    "-b",
    "--base",
    action="store_true",
    default=True,
    help="Добавление base для моделей",
)
parser.add_argument(
    "-c",
    "--config",
    action="store_true",
    default=True,
    help="Добавление config и env файлов",
)

args = parser.parse_args()
controller.handle(args)
