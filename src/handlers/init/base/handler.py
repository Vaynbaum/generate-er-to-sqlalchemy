import os

from src.handlers.init.base.const import *
from src.handlers.init.interface import IInitHandler, InitConfig


class BaseInitHandler(IInitHandler):
    def __process_template(self, template: str, config: InitConfig):
        kwargs = {
            FORMAT_URL_DB: URL_DB,
            FORMAT_IMPORT_SETTINGS: "",
            FORMAT_IMPORT_BASE: "",
            FORMAT_ADD_BASE: "",
            FORMAT_CONNECT_ARGS: CONNECT_ARGS,
        }

        if config.add_config_file:
            kwargs[FORMAT_URL_DB] = URL_DB.replace(REPLACE_SETS_BRACKET, INSERT_SETS)
            kwargs[FORMAT_IMPORT_SETTINGS] = IMPORT_SETTINGS

        if config.add_base_file:
            kwargs[FORMAT_IMPORT_BASE] = IMPORT_BASE
            kwargs[FORMAT_ADD_BASE] = ADD_BASE
        template = template.format(**kwargs)
        return template

    def handle(self, config: InitConfig):
        base_file_path = os.path.join(config.root_path, DEFAULT_NAME_FILE_BASE)
        if not os.path.exists(base_file_path):
            path = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(path, NAME_TEMPLATE), "r") as template_file:
                template = self.__process_template(template_file.read(), config)
            with open(base_file_path, "w") as base_file:
                base_file.write(template)
