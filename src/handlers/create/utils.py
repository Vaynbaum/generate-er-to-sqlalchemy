import os
import re


PATTERN_CAMEL_SNAKE = re.compile(r"(?<!^)(?=[A-Z])")
PATTERN_INI_FILE = re.compile(r"\[(.*?)\]\s+([\w\W]*?)(?=\n\[|$)")


def camel_to_snake(s: str):
    return PATTERN_CAMEL_SNAKE.sub("_", s).lower()

def path_to_python_import(path:str):
    path = path.replace(os.sep, '.')
    return path
    
def clear_str_from_tag(s: str):
    return re.sub(r"<.*?>", "", s).replace(" ", "")


def field_id_from_tablename(tablename: str):
    return f"{tablename[:-1]}_id"


def ini_file_to_dict(contents: str):
    matches = re.findall(PATTERN_INI_FILE, contents)
    result = {}
    for match in matches:
        key = match[0]
        value = match[1].strip()
        result[key] = value

    return result
