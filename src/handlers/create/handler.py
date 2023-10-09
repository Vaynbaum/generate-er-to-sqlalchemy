import os

from src.const import *
from src.handlers.create.const import *
from src.handlers.create.interface import *
from src.handlers.interface import IHandler
from src.interface import ArgConfig


class CreateModelHandler(IHandler):
    def __init__(self, parser: IDiagramParser, creater: IModelCreater):
        super().__init__(ACTION_CREATE)
        self.__parser = parser
        self.__creater = creater

    def handle(self, config: ArgConfig):
        app_path = config.app_path
        if app_path:
            name_page = config.page_name or DEFAULT_NAME_PAGE
            parser_config = ParserConfig(file_path=config.er_file, name_page=name_page)
            tables, id = self.__parser.handle(parser_config)

            app_path = os.path.abspath(app_path)
            path_ini_file = os.path.join(app_path, NAME_FILE_INI)
            self.__creater.handle(tables, path_ini_file, id)
            return ACTION_SUCCESS
        return NOT_FOUND_PATH_APP
