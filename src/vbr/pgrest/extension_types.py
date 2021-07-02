import uuid
from hashids import Hashids
from .column import PgRestColumn
from .types import *

# TODO - Move this outside of the pgrest module

__all__ = ['LocalId', 'new_hashid']

HASH_SALT = '*<rjFeB$Fy2#~-H@'


def new_hashid(salt=None):
    """Return a new, randomly-generated hashid
    """
    if salt is None:
        salt = HASH_SALT
    hashids = Hashids(salt=salt)
    _uuid = uuid.uuid1().int >> 64
    return hashids.encode(_uuid)


class AutoPopulate(object):
    @classmethod
    def autopopulate(cls, value):
        return value


class AutoHashId(AutoPopulate):

    SALT = None

    @classmethod
    def autopopulate(cls, value):
        if value is not None:
            return cls.validated(value)
        else:
            if cls.SALT is not None:
                salt = cls.SALT
            else:
                salt = HASH_SALT
            return new_hashid(salt=salt)

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
