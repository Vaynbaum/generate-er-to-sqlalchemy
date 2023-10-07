from src.handlers.interface import IHandler
from src.interface import ArgConfig


class MainController:
    def __init__(self, handlers: dict[IHandler]):
        self.__handlers = handlers

    def handle(self, args):
        config = ArgConfig(
            add_config_file=args.config,
            add_base_file=args.base,
            app_name=args.name,
            action=args.action,
            er_file=args.er_file,
            name_page=args.page_name,
        )
        if config.action:
            handler = self.__handlers.get(config.action, None)
            if handler:
                handler.handle(config)
