import os

from src.handlers.init.interface import IInitHandler, InitConfig
from src.handlers.init.const import *
from src.const import *
from src.interface import ArgConfig
from src.handlers.interface import *


class InitHandler(IHandler):
    def __init__(self, handlers: list[IInitHandler]):
        self.__handlers = handlers

    def handle(self, config: ArgConfig):
        if config.action == INIT:
            self.__create(config)

    def __create_main_dirs(self, root_path):
        path = f"{root_path}/"
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

    def __create(self, config: ArgConfig):
        app_path, src_path, root_path, models_path = self._build_path_models(config)
        self.__create_main_dirs(models_path)

        init_config = InitConfig(
            root_path=root_path, src_path=src_path, app_path=app_path, **config.dict()
        )
        for handler in self.__handlers:
            handler.handle(init_config)
