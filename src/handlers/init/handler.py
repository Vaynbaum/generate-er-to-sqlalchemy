import os

from src.const import *
from src.handlers.init.const import *
from src.handlers.interface import *


class InitHandler(IHandler):
    def __init__(self):
        super().__init__(ACTION_INIT)

    def handle(self, config: ArgConfig):
        app_path = config.app_path
        if app_path:
            app_path, dir_database = self.__define_paths(config, app_path)
            models_path = self.__init_dir_models(dir_database)
            self.__create_dirs_gemodels(models_path)
            base_path = self.__init_base_file(dir_database)
            self.__crawling(dir_database, NAME_FILE_INIT_PY)
            self.__create_init_file(app_path, base_path, models_path)
            return ACTION_SUCCESS
        return NOT_FOUND_PATH_APP

    def __define_paths(self, config: ArgConfig, app_path: str):
        app_path = os.path.abspath(app_path)
        if config.dir_database:
            dir_database = os.path.abspath(config.dir_database)
        else:
            dir_database = os.path.join(app_path, DEFAULT_DATABASE_PATH)
        return app_path, dir_database

    def __create_dirs_gemodels(self, models_path: str):
        self.__create_directory(os.path.join(models_path, NAME_DIR_AUTO_GEMODELS))
        self.__create_directory(os.path.join(models_path, NAME_DIR_USER_GEMODELS))

    def __create_init_file(self, app_path: str, base_path: str, models_path: str):
        path = os.path.join(app_path, NAME_FILE_INI)
        spliter = f"{app_path}\\"
        models_path = models_path.split(spliter)[1]
        init_py = os.path.join(models_path, NAME_FILE_INIT_PY)
        auto = os.path.join(models_path, NAME_DIR_AUTO_GEMODELS)
        user = os.path.join(models_path, NAME_DIR_USER_GEMODELS)

        with open(path, "w", encoding="utf8") as f:
            f.write(f"[{KW_APP}]\n{app_path}\n")
            f.write(f"\n[{KW_BASE}]\n{base_path.split(spliter)[1]}\n")
            f.write(f"\n[{KW_INIT_PY}]\n{init_py}\n")
            f.write(f"\n[{KW_AUTO}]\n{auto}\n")
            f.write(f"\n[{KW_USER}]\n{user}\n")

    def __init_base_file(self, dir_database: str):
        path = os.path.join(dir_database, NAME_FILE_BASE)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(f"{IMPORT_BASE}\n\n{ADD_BASE}")
        else:
            with open(path, "r") as f:
                data = f.read()
            if not (IMPORT_BASE in data and ADD_BASE in data):
                with open(path, "w") as f:
                    f.write(f"{IMPORT_BASE}\n{data}\n{ADD_BASE}")
        return path

    def __init_dir_models(self, dir_database: str):
        models_path = os.path.join(dir_database, NAME_DIR_MODELS)
        self.__create_directory(models_path)
        return models_path

    def __crawling(self, root: str, file_path: str):
        path = os.path.join(root, file_path)
        if not os.path.exists(path):
            open(path, "w")

        for item in os.listdir(root):
            path_item = os.path.join(root, item)
            if os.path.isdir(path_item):
                self.__crawling(path_item, file_path)

    def __create_directory(self, path: str):
        path += "\\"
        is_exists = not os.path.exists(os.path.dirname(path))
        if is_exists:
            os.makedirs(os.path.dirname(path))
        return is_exists
