NAME_TEMPLATE = "template.py"
DEFAULT_NAME_FILE_BASE = "base.py"

FORMAT_IMPORT_SETTINGS = "import_settings"
FORMAT_CONNECT_ARGS = "connect_args"
FORMAT_IMPORT_BASE = "import_base"
FORMAT_ADD_BASE = "add_base"
FORMAT_URL_DB = "url_db"

IMPORT_SETTINGS = "from src.config import settings"
IMPORT_BASE = "from sqlalchemy.ext.declarative import declarative_base"

REPLACE_SETS_BRACKET = "{"
INSERT_SETS = "{settings."

ADD_BASE = "Base = declarative_base()"
URL_DB = "{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{POSTGRES_DB}"
CONNECT_ARGS = {"check_same_thread": False}
