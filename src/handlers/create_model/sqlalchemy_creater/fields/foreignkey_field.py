from fields.integer_field import IntegerSQLAlchemyField


class ForeignKeySQLAlchemyField(IntegerSQLAlchemyField):
    def __init__(
        self,
        name: str,
        is_primary_key: bool = False,
        is_nullable: bool = True,
        is_unique: bool = False,
    ):
        ...
