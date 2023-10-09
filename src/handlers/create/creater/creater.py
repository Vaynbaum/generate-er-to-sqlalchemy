import os

from src.const import *
from src.handlers.create.const import *
from src.handlers.create.creater.const import *
from src.handlers.create.interface import IModelCreater, TableFromDiagramSchema
from src.handlers.create.utils import ini_file_to_dict, path_to_python_import


class SQLAlchemyModelCreater(IModelCreater):
    def handle(self, tables: list[TableFromDiagramSchema], path_ini_file: str, id: str):
        with open(path_ini_file, "r", encoding="utf8") as file:
            ini_data = file.read()
            ini_data = ini_file_to_dict(ini_data)

        for table in tables:
            self.__create_auto_gemodel(table, ini_data, id)
            self.__create_user_gemodel(table, ini_data)
            self.__add_item_to_init_file(table, ini_data)
        self.__remove_died_files(tables, ini_data, id)

    def __add_item_to_init_file(self, table: TableFromDiagramSchema, ini_data: dict):
        path_init_file = os.path.join(ini_data[KW_APP], ini_data[KW_INIT_PY])
        path_user_model_file = os.path.join(ini_data[KW_USER], table.file_name)
        path_user_model_file = path_to_python_import(path_user_model_file)[:-3]
        import_str = f"from {path_user_model_file} import {table.class_name} as {table.class_name}\n"

        with open(path_init_file, "r+", encoding="utf8") as file:
            imports = file.readlines()
            if not import_str in imports:
                file.write(import_str)

    def __remove_died_files(
        self, tables: list[TableFromDiagramSchema], ini_data: dict, id: str
    ):
        table_names = {table.file_name: table.class_name for table in tables}
        root = os.path.join(ini_data[KW_APP], ini_data[KW_AUTO])
        path_init_py = os.path.join(ini_data[KW_APP], ini_data[KW_INIT_PY])
        with open(path_init_py, "r", encoding="utf8") as file_init_py:
            imports = file_init_py.read()

        for auto_files in os.listdir(root):
            path_item = os.path.join(root, auto_files)

            if os.path.isfile(path_item):
                with open(path_item, "r", encoding="utf8") as file:
                    content = file.read()

                if id in content and not auto_files in table_names:
                    os.remove(path_item)
                    path_user_model = os.path.join(
                        ini_data[KW_APP], ini_data[KW_USER], auto_files
                    )
                    os.remove(path_user_model)

                    path_user_model = os.path.join(ini_data[KW_USER], auto_files)
                    path_user_model = path_to_python_import(path_user_model)[:-3]
                    imprts = imports.splitlines()
                    import_str = ""
                    for i in imprts:
                        if path_user_model in i:
                            import_str = i
                            break
                    imports = imports.replace(f"{import_str}\n", "")

        with open(path_init_py, "w", encoding="utf8") as file_init_py:
            file_init_py.write(imports)

    def __create_user_gemodel(self, table: TableFromDiagramSchema, ini_data: dict):
        path_file = os.path.join(ini_data[KW_APP], ini_data[KW_USER], table.file_name)
        if not os.path.exists(path_file):
            path_template = os.path.dirname(os.path.abspath(__file__))
            with open(
                os.path.join(path_template, DIR_TEMPLATES, FILE_TMPLT_USER_GM)
            ) as f:
                template = f.read()

            cnfg = {
                "auto_gemodel_import": path_to_python_import(
                    os.path.join(ini_data[KW_AUTO], table.file_name)[:-3]
                ),
                "class_name": table.class_name,
                "class_name_auto_gemodel": f"{PREFIX_CLASS}{table.class_name}",
            }
            model_content = template.format(**cnfg)
            with open(path_file, "w") as model_file:
                model_file.write(model_content)

    def __create_auto_gemodel(
        self, table: TableFromDiagramSchema, ini_data: dict, id: str
    ):
        path_template = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_template, DIR_TEMPLATES, FILE_TMPLT_AUTO_GM)) as f:
            template = f.read()

        path_file = os.path.join(ini_data[KW_APP], ini_data[KW_AUTO], table.file_name)
        base_path = path_to_python_import(ini_data[KW_BASE])[:-3]
        (
            fields,
            type_imports,
            any_imports,
            relations,
            is_rel_import,
        ) = self.__proccess_fields(table, path_to_python_import(ini_data[KW_USER]))
        if is_rel_import:
            type_imports = type_imports + f"\n{IMPORT_RELATIONSHIP}\n"

        if os.path.exists(path_file):
            with open(path_file, "r") as f:
                model_content_old = f.read()
            any_imports, relations = self.__save_relations(
                any_imports, relations, fields, model_content_old
            )

        cnfg = {
            "imports": type_imports,
            "base_path": base_path,
            "class_name": f"{PREFIX_CLASS}{table.class_name}",
            "table_name": table.tablename,
            "any_imports": any_imports,
            "fields": fields,
            "relations": relations,
        }
        model_content = template.format(**cnfg)
        with open(path_file, "w") as model_file:
            model_file.write(f'"{id}"\n')
            model_file.write(model_content)

    def __save_relations(
        self, any_imports: str, relations: str, fields: str, model_content_old: str
    ):
        old_any_imports = model_content_old.split("any_imports\n")[1]
        old_imports = old_any_imports.split("class")[0].split("\n")
        old_relations = model_content_old.split("relations\n")[1].split("\n")

        for r in old_relations:
            if r:
                class_name = r.split("relationship(")[1].split(",")[0]
                if not class_name in fields:
                    relations += f"{r}"
        for i in old_imports:
            if i:
                class_name = i.split("import ")[1]
                if not class_name in fields:
                    any_imports += f"{i}"

        return any_imports, relations

    def __proccess_fields(self, table: TableFromDiagramSchema, import_path: str):
        content = ""
        type_imports = set()
        str_type_imports = ""
        any_imports = ""
        relations = ""
        is_rel_import = False
        type_imports.add(COLUMN)

        for field in table.fields:
            type = field.type.upper()
            type_imports.add(type.split("(")[0])
            content += f"{TABULATION}{field.name} = {COLUMN}({type}"
            if field.is_fk:
                type_imports.add(FOREIGNKEY)
                if field.fk_table:
                    any_imports += f"from {import_path}.{field.fk_table.file_name[:-3]} import {field.fk_table.class_name}\n"
                    content += f", {FOREIGNKEY}({field.fk_table.class_name}.{field.fk_table.fields[0].name})"
                    is_rel_import = True
                    relations += f'{TABULATION}{field.name[:-3]} = relationship({field.fk_table.class_name}, backref=backref("{table.tablename}", cascade="all, delete-orphan"))\n'

            if field.is_primary:
                content += f", primary_key={field.is_primary}"
            if field.is_not_null:
                content += f", nullable={field.is_not_null}"
            if field.is_unique:
                content += f", unique={field.is_unique}"
            if field.default:
                content += f", default={field.default.title()}"
            content += f")\n"

        for t in type_imports:
            str_type_imports += f"{t}, "

        return (
            content[:-1],
            str_type_imports[:-2],
            any_imports,
            relations,
            is_rel_import,
        )
