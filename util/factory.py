from const import *
from main_controller import MainController
from handlers.init import *
from handlers.create import *


def create_model_handler():
    return CreateModelHandler(DrawERParser(), SQLAlchemyModelCreater())


def create_init_handler():
    return InitHandler()


def create_main_controller():
    return MainController([create_init_handler(), create_model_handler()])
