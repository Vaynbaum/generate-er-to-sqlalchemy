from pydantic import BaseModel
from abc import ABC, abstractmethod


class InitConfig(BaseModel):
    add_config_file: bool | None = True
    add_base_file: bool | None = True
    app_name: str | None = None
    root_path: str | None = ""
    src_path: str | None = ""
    app_path: str | None = ""


class IInitHandler(ABC):
    @abstractmethod
    def handle(self, config: InitConfig):
        raise NotImplementedError()
