from ..pgrest import PgRestColumn

__all__ = ["LocalId"]


class LocalId(PgRestColumn):
    DATA_TYPE = "varchar"
    PYTHON_TYPE = str
    CHAR_LEN = 10

    @classmethod
    def instantiate(cls, value):
        if value is not None:
            return value
        else:
            return "0xDEADBEEF"
