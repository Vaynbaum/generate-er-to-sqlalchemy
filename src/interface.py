from pydantic import BaseModel


class ArgConfig(BaseModel):
    add_config_file: bool | None = True
    add_base_file: bool | None = True
    app_name: str | None = None
    action: str | None = ""
    er_file: str | None = ""
    name_page: str | None = ""
