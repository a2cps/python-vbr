from .column import PgRestColumn
from .utils import class_or_instancemethod

__all__ = [
    'Boolean', 'DateTime', 'Integer', 'IntegerList', 'Serial', 'String',
    'StringList', 'Text', 'TimeStamp', 'CreatedTimeStamp', 'UpdatedTimeStamp'
]


class Boolean(PgRestColumn):
    DATA_TYPE = 'boolean'
    PYTHON_TYPE = bool


class DateTime(PgRestColumn):
    DATA_TYPE = 'datetime'


class Integer(PgRestColumn):
    DATA_TYPE = 'integer'
    PYTHON_TYPE = int


class IntegerList(PgRestColumn):
    DATA_TYPE = 'int[]'
    PYTHON_TYPE = None


class Serial(PgRestColumn):
    DATA_TYPE = 'serial'
    PYTHON_TYPE = int


class String(PgRestColumn):
    DATA_TYPE = 'varchar'
    PYTHON_TYPE = str
    CHAR_LEN = 255

    def __init__(self, max_size=None):
        self.CHAR_LEN = max_size

    @class_or_instancemethod
    def properties(self_or_cls):
        return {
            'data_type': self_or_cls.DATA_TYPE,
            'char_len': self_or_cls.CHAR_LEN
        }


class StringList(PgRestColumn):
    DATA_TYPE = 'varchar[]'
    PYTHON_TYPE = None


class Text(PgRestColumn):
    DATA_TYPE = 'text'
    PYTHON_TYPE = str


class TimeStamp(PgRestColumn):
    DATA_TYPE = 'timestamp'
    PYTHON_TYPE = str


class CreatedTimeStamp(TimeStamp):
    @class_or_instancemethod
    def properties(self_or_cls):
        return {'data_type': self_or_cls.DATA_TYPE, 'default': 'CREATETIME'}


class UpdatedTimeStamp(TimeStamp):
    @class_or_instancemethod
    def properties(self_or_cls):
        return {'data_type': self_or_cls.DATA_TYPE, 'default': 'UPDATETIME'}
