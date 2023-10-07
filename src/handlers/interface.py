from abc import ABC, abstractmethod
import os

from src.const import *
from src.interface import ArgConfig


class IHandler(ABC):
    def _build_path_models(self, config: ArgConfig):
        app_path = config.app_name or DEFAULT_APP_NAME
        src_path = os.path.join(app_path, DEFAULT_SRC_PATH)
        root_path = os.path.join(src_path, DEFAULT_DATABASE_PATH)
        models_path = os.path.join(root_path, DEFAULT_MODELS_PATH)
        return app_path, src_path, root_path, models_path

    @abstractmethod
    def handle(self, config: ArgConfig):
        raise NotImplementedError()
