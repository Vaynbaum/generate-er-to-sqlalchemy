import os

from src.handlers.init.interface import IInitHandler, InitConfig
from src.handlers.init.config.const import *
from src.handlers.init.const import *


class ConfigInitHandler(IInitHandler):
    def __process_template(self, template: str):
        kwargs = {FORMAT_FILE_ENV: DEFAULT_NAME_FILE_ENV}
        template = template.format(**kwargs)
        return template

    def handle(self, config: InitConfig):
        if not config.add_config_file:
            return
        config_file_path = os.path.join(config.src_path, DEFAULT_NAME_FILE_CONFIG)
        if not os.path.exists(config_file_path):
            path = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(path, NAME_TEMPLATE)) as template_file:
                template = self.__process_template(template_file.read())
            with open(config_file_path, "w") as config_file:
                config_file.write(template)
