import argparse

from src.const import *
from src.factory import create_main_controller


controller = create_main_controller()
action_help = "Select a program action"
dir_help = "A directory inside the application with a connection to the database, a directory with models (e.g. app/src/database)"
page_name_help = "Name of the page with the diagram"
parser = argparse.ArgumentParser(description="Program Description")
parser.add_argument("action", choices=controller.get_actions(), help=action_help)
parser.add_argument("-a", "--app_path", type=str, help="The path to the application")
parser.add_argument("-d", "--dir_database", type=str, help=dir_help)
parser.add_argument("-e", "--er_file", type=str, help="Draw io file with ER diagram")
parser.add_argument("-p", "--page_name", type=str, help=page_name_help)


args = parser.parse_args()
controller.handle(args)
