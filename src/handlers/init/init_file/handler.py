import os
import shutil

from src.handlers.init.interface import IInitHandler, InitConfig
from src.handlers.init.init_file.const import NAME_TEMPLATE


class InitFileInitHandler(IInitHandler):
    def __crawling(self, root: str, file_path: str):
        self.__create_file(root, file_path)
        for item in os.listdir(root):
            path_item = os.path.join(root, item)

            if os.path.isdir(path_item):
                self.__crawling(path_item, file_path)

    def __create_file(self, root: str, file_path: str):
        dest_path = os.path.join(root, NAME_TEMPLATE)
        if not os.path.exists(dest_path):
            shutil.copy2(file_path, dest_path)

    def handle(self, config: InitConfig):
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(path, NAME_TEMPLATE)
        self.__crawling(config.src_path, file_path)
