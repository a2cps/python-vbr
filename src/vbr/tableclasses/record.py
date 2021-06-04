import datetime
import logging
import pytz
from typing import Any

from .. import constants
from .. import errors
from ..utils import timestring_to_timestamp

logging.basicConfig(level=logging.DEBUG)

SESSION_FIELD = 'internal_session'

__all__ = ['VBRRecord', 'SESSION_FIELD']


class VBRRecord:
    """A Virtual Biospecimen Repository table record

    To use:
    >>> vb = VBRRecord()
    >>> vb.table_name
    default
    >>> vb.primary_key
    None
    >>> vb.field_names()
    ()
    >>> vb.field_values()
    ()
    """
    # Name of the PostgreSQL table mapped by the class
    TABLE = 'default'
    # Alias for the table, used in PgREST
    TABLE_ALIAS = None
    # Name of the table's primary, serial key
    PRIMARY_KEY = None
    # Field definitions (name, type, required)
    FIELDS = []

    def _to_serial(self, value: Any) -> int:
        """Cast to serial (integer)
        """
        if self.new is True:
            return None
        else:
            return int(value)

    def _to_varchar(self, value: Any) -> str:
        """Cast to varchar
        """
        if value is None:
            return value
        else:
            return str(value)

    def _to_integer(self, value: Any) -> int:
        """Cast to integer
        """
        if value is None:
            return value
        else:
            return int(value)

    def _to_boolean(self, value: Any) -> bool:
        """Cast to boolean
        """
        if value is None:
            return value
        else:
            return bool(value)

    def _to_timestamp(self, value: Any) -> datetime.datetime:
        """Cast to datetime
        """
        if value is None:
            return value
        else:
            if isinstance(value, datetime.datetime):
                tz = pytz.timezone(self.tz2)
                # Try to localize naive datetime
                try:
                    return tz.localize(value)
                except ValueError:
                    return value
            elif isinstance(value, str):
                return timestring_to_timestamp(value, self.tz1, self.tz2)

    def __init__(self,
                 new: bool = True,
                 tz1: str = constants.SOURCE_TIMEZONE,
                 tz2: str = constants.DATABASE_TIMEZONE,
                 **kwargs):

        # Holds values for the record object
        self._VALUES = {}

        # If set, we don't expect the primary, serial key to be provided
        self.new = new

        # Allows for conversion of timezone while casting time string to datetime
        self.tz1 = tz1
        self.tz2 = tz2

        if len(self.fields()) > 0:
            for field_name, sql_type, required in self.fields():
                if required is True and field_name not in kwargs:
                    raise errors.ValidationError(
                        '{0} is required but was not provided'.format(
                            field_name))
                self._VALUES[field_name] = kwargs.pop(field_name, None)
            if len(kwargs.items()) > 0:
                raise errors.ValidationError(
                    'Cannot process unknown kwargs: {0}'.format(kwargs))
        logging.debug('VBRRecord: {0}'.format(self._VALUES))

    @classmethod
    def table_name(cls) -> str:
        """The name of the VBR table mapped by this class
        """
        return cls.TABLE

    @classmethod
    def table_alias(cls) -> str:
        """An alias for VBR table mapped by this class
        """
        if cls.TABLE_ALIAS is not None:
            return cls.TABLE_ALIAS
        else:
            return cls.TABLE

    @classmethod
    def primary_key(cls) -> str:
        return cls.PRIMARY_KEY

    @classmethod
    def fields(cls) -> dict:
        return cls.FIELDS

    @classmethod
    def field_names(cls, include_pk: bool = False) -> tuple:
        """Ordered names of fields in self.TABLE for use with DBMS
        """
        fnames = []
        if len(cls.fields()) > 0:
            for field_name, sql_type, required in cls.fields():
                if field_name != cls.PRIMARY_KEY or include_pk is True:
                    fnames.append(field_name)
        return tuple(fnames)

    def field_values(self, include_pk: bool = False) -> tuple:
        """Render record as tuple of values for use with DBMS
        """
        fvals = []
        if len(self.fields()) > 0:
            for field_name, sql_type, required in self.fields():
                if field_name != self.PRIMARY_KEY or include_pk is True:
                    func = getattr(self, '_to_' + sql_type)
                    value = func(self._VALUES.get(field_name))
                    fvals.append(value)
        return tuple(fvals)

    def get_field(self, field_name: str) -> Any:
        if field_name in self.field_names(include_pk=True):
            return self._VALUES.get(field_name, None)
        else:
            raise errors.ValidationError(
                '{0} is not gettable from table {1}'.format(
                    field_name, self.table_name))

    def set_field(self, field_name: str, field_value: Any) -> Any:
        if field_name in self.field_names():
            self._VALUES[field_name] = field_value
            return field_value
        else:
            raise errors.ValidationError(
                '{0} is not settable in table {1}'.format(
                    field_name, self.table_name))

    def validate(self) -> bool:
        """Validate the object's data fields
        """
        try:
            self.field_values()
            return True
        except Exception as exc:
            logging.warning(str(exc))
            return False
