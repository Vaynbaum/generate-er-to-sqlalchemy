import json


from src.const import CREATE_MODEL
from src.handlers.create_model.const import DEFAULT_NAME_PAGE
from src.handlers.create_model.interface import *
from src.handlers.interface import IHandler
from src.interface import ArgConfig


class CreateModelHandler(IHandler):
    def __init__(self, parser: IDiagramParser, creater: IModelCreater):
        self.__parser = parser
        self.__creater = creater

    def handle(self, config: ArgConfig):
        if config.action == CREATE_MODEL:
            tables = self.__create(config)
            self.__creater.handle(tables)

    def __create(self, config: ArgConfig):
        parser_config = ParserConfig(
            file_path=config.er_file,
            name_page=config.name_page or DEFAULT_NAME_PAGE,
            path=self._build_path_models(config)[3],
        )
        return self.__parser.handle(parser_config)

        # with open("er.json", "w") as f:
        #     f.write(json.dumps(data))
