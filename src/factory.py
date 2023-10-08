from src.const import *
from src.main_controller import MainController
from src.handlers.init import *
from src.handlers.create import *


def create_model_handler():
    return CreateModelHandler(DrawERParser(), SQLAlchemyModelCreater())


def create_init_handler():
    return InitHandler()


def create_main_controller():
    return MainController([create_init_handler(), create_model_handler()])
