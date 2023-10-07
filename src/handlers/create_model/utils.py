import re


pattern = re.compile(r"(?<!^)(?=[A-Z])")


def camel_to_snake(s: str):
    return pattern.sub("_", s).lower()


def clear_str_from_tag(s: str):
    return re.sub(r"<.*?>", "", s).replace(" ", "")


def field_id_from_tablename(tablename: str):
    return f"{tablename[:-1]}_id"
