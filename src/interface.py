from pydantic import BaseModel


class ArgConfig(BaseModel):
    action: str | None = None
    app_path: str | None = None
    dir_database: str | None = None
    er_file: str | None = None
    page_name: str | None = None
