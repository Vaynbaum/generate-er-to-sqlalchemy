from src.handlers.interface import IHandler
from src.interface import ArgConfig


class MainController:
    def __init__(self, handlers: list[IHandler]):
        self.__handlers = {h.action: h for h in handlers}

    def get_actions(self):
        return [k for k in self.__handlers.keys()]

    def handle(self, args):
        config = ArgConfig(
            action=args.action,
            app_path=args.app_path,
            dir_database=args.dir_database,
            er_file=args.er_file,
            page_name=args.page_name,
        )
        if config.action:
            handler = self.__handlers.get(config.action, None)
            if handler:
                msg = handler.handle(config)
            print(msg)
