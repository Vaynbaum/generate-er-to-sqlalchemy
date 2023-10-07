import os
import shutil

from src.handlers.init.interface import IInitHandler, InitConfig
from src.handlers.init.config.const import *
from src.handlers.init.const import *
from src.handlers.init.env.const import NAME_TEMPLATE


class EnvInitHandler(IInitHandler):
    def handle(self, config: InitConfig):
        if not config.add_config_file:
            return

        path = os.path.dirname(os.path.abspath(__file__))
        env_file_path = os.path.join(config.app_path, DEFAULT_NAME_FILE_ENV)

        if not os.path.exists(env_file_path):
            shutil.copy2(os.path.join(path, NAME_TEMPLATE), env_file_path)
