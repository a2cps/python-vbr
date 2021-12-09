import datetime
import re
from os import statvfs

from .column import PgRestColumn
from .utils import class_or_instancemethod, datetime_to_isodate

__all__ = [
    "Boolean",
    "Date",
    "Numeric",
    "GUID",
    "Integer",
    "IntegerList",
    "Serial",
    "String",
    "StringList",
    "Text",
    "TimeStamp",
    "CreatedTimeStamp",
    "UpdatedTimeStamp",
    "FreeText",
]


class Boolean(PgRestColumn):
    DATA_TYPE = "boolean"
    PYTHON_TYPE = bool

    @classmethod
    def cast(cls, value):
        if value is None or value == "":
            return None
        else:
            return bool(int(value))


class Date(PgRestColumn):
    DATA_TYPE = "date"
    # TODO - validate by reading string into a datetime, confirming trailing Z

    @classmethod
    def cast(cls, value):
        if value is None or value == "":
            return None
        else:
            if isinstance(value, datetime.datetime):
                value = datetime_to_isodate(value)
            # TODO - other date transformations
            return value


class Integer(PgRestColumn):
    DATA_TYPE = "integer"
    PYTHON_TYPE = int

    @classmethod
    def instantiate(cls, value):
        if value is None or value == "":
            return None
        else:
            return int(value)

    @classmethod
    def cast(cls, value):
        if value is None or value == "":
            return None
        else:
            return int(value)


class IntegerList(PgRestColumn):
    DATA_TYPE = "int[]"
    PYTHON_TYPE = None
    # TODO - validate that contents of data are a list of ints


# class Numeric(PgRestColumn):
#     DATA_TYPE = 'numeric'
#     PYTHON_TYPE = float

#     # TODO Support numeric(p,s), a real number with p digits with s number after the decimal point.
#     @classmethod
#     def instantiate(cls, value):
#         if value is None or value == '':
#             return None
#         else:
#             return float(value)

#     @classmethod
#     def cast(cls, value):
#         if value is None or value == '':
#             return None
#         else:
#             return float(value)


class Numeric(PgRestColumn):
    # NOTE - this is currently implemented as a postgresql varchar because PgREST doesn't support numeric type
    DATA_TYPE = "varchar"
    PYTHON_TYPE = float
    CHAR_LEN = 32

    @class_or_instancemethod
    def properties(self_or_cls):
        return {"data_type": self_or_cls.DATA_TYPE, "char_len": self_or_cls.CHAR_LEN}

    # TODO Support numeric(p,s), a real number with p digits with s number after the decimal point.
    @classmethod
    def instantiate(cls, value):
        if value is None or value == "":
            return None
        else:
            return str(float(value))

    @classmethod
    def cast(cls, value):
        if value is None or value == "":
            return None
        else:
            return str(float(value))


class Serial(Integer):
    DATA_TYPE = "serial"
    # PYTHON_TYPE = int
    @class_or_instancemethod
    def properties(self_or_cls):
        return {
            "data_type": self_or_cls.DATA_TYPE,
            "serial_start": 1000,
            "serial_increment": 1,
        }


class String(PgRestColumn):
    DATA_TYPE = "varchar"
    PYTHON_TYPE = str
    CHAR_LEN = 255

    def __init__(self, max_size=None):
        self.CHAR_LEN = max_size

    @class_or_instancemethod
    def properties(self_or_cls):
        return {"data_type": self_or_cls.DATA_TYPE, "char_len": self_or_cls.CHAR_LEN}

    @classmethod
    def cast(cls, value):
        if value is None:
            return None
        else:
            return str(value)


class FreeText(String):
    CHAR_LEN = 1024

    @classmethod
    def cast(cls, value):
        """Formats a long string value into a sanitized and escaped single line"""
        value = super().cast(value)
        value = re.sub(r"\s+", " ", value, flags=re.MULTILINE)
        # HACK This is to work around annoying edge case in json
        # specs that differ materially on if and how
        # single-quote characters must be escaped.
        value = re.sub(r"'", "", value, flags=re.MULTILINE)
        value = value.strip()
        return value


class StringList(PgRestColumn):
    DATA_TYPE = "varchar[]"
    PYTHON_TYPE = None
    # TODO - validate that contents of data are a list of strings


class Text(String):
    DATA_TYPE = "text"


class GUID(String):
    # Placeholder for GUID dedicated type
    pass


class TimeStamp(PgRestColumn):
    DATA_TYPE = "timestamp"
    PYTHON_TYPE = str
    # TODO - validate that contents of default are a datetime string
    #        or are in (CREATETIME, UPDATETIME)


class CreatedTimeStamp(TimeStamp):
    @class_or_instancemethod
    def properties(self_or_cls):
        return {"data_type": self_or_cls.DATA_TYPE, "default": "CREATETIME"}


class UpdatedTimeStamp(TimeStamp):
    @class_or_instancemethod
    def properties(self_or_cls):
        return {"data_type": self_or_cls.DATA_TYPE, "default": "UPDATETIME"}
