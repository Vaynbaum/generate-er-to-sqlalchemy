# import os

# from src.env.env import EnvChart
# from src.interfaces import BaseConfig, ChartConfig, IBaseDatabase
# from src.const import *
# from src.table.table import IBaseTable


# class Chart:
#     def __init__(self, base_cls: IBaseDatabase, config: ChartConfig):
#         app_name = config.app_name or DEFAULT_APP_NAME
#         src_path = os.path.join(app_name, DEFAULT_SRC_PATH)
#         self._root_path = os.path.join(src_path, DEFAULT_DATABASE_PATH)

#         base_config = BaseConfig(path=self._root_path, **config.dict())
#         self._base: IBaseDatabase = base_cls(base_config)
#         if config.add_config_file:
#             base_config = base_config.copy()
#             base_config.path = src_path
#             self._env = EnvChart(base_config)
#         self._tables: list[IBaseTable] = []

#         self.init_app(config)

#     def init_app(self, config: ChartConfig):
#         path = f"{self._root_path}/"
#         if not os.path.exists(os.path.dirname(path)):
#             os.makedirs(os.path.dirname(path))

#         self._base.generate()
#         if config.add_config_file:
#             self._env.generate()

#     def add_table(self, table: IBaseTable):
#         self._tables.append(table)

#     def delete_table(self, table: IBaseTable):
#         self._tables.remove(table)

#     def generate(self) -> str:
#         raise NotImplementedError()
