import uuid
from hashids import Hashids
from .column import PgRestColumn
from .types import *

# TODO - Move this outside of the pgrest module

__all__ = ['LocalId']

class AutoPopulate(object):

    @classmethod
    def autopopulate(cls, value):
        return value

class AutoHashId(AutoPopulate):

    HASH_SALT = '*<rjFeB$Fy2#~-H@'
    
    @classmethod
    def autopopulate(cls, value):
        if value is not None:
            return cls.validated(value)
        else:
            hashids = Hashids(salt=cls.HASH_SALT)
            _uuid = uuid.uuid1().int >> 64
            return hashids.encode(_uuid)

    @classmethod
    def validated(cls, value):
        """Returns value if valid, raises ValueError if not
        """
        hashids = Hashids(salt=cls.HASH_SALT)
        dec = hashids.decode(value)
        if len(dec) > 0:
            return value
        else:
            raise ValueError('{0} is not a valid hashid'.format(value))

class LocalId(String, AutoHashId):
    """Extension of String that automatically populates its value with a HashId
    """
    DATA_TYPE = 'varchar'
    PYTHON_TYPE = str
    CHAR_LEN = 16

    @classmethod
    def instantiate(cls, value):
        return cls.autopopulate(value)
