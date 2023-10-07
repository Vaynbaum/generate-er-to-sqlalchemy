from src.const import *
from src.main_controller import MainController
from src.handlers.init import *
from src.handlers.create_model import *


def create_model_handler():
    return CreateModelHandler(DrawERParser())


def create_init_handler():
    return InitHandler(
        [
            BaseInitHandler(),
            EnvInitHandler(),
            ConfigInitHandler(),
            InitFileInitHandler(),
        ]
    )


def create_main_controller():
    return MainController(
        {INIT: create_init_handler(), CREATE_MODEL: create_model_handler()}
    )
