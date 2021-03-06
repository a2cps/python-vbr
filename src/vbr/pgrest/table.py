import copy
import datetime
import json

from .column import Column
from .constraints import Constraint
from .enums import Enumeration
from .schema import PgrestSchema
from .utils import datetime_to_isodate

__all__ = ["Table", "AssociationTable"]


class Table(object):
    """PgREST Table"""

    __tablename__ = None
    __rooturl__ = None

    # TODO - support for generating create/update JSON for PgREST

    def __init__(self, table_id=None, **kwargs):

        self.__table_id__ = table_id
        self.__class_attrs__ = {}
        self.__schema__ = PgrestSchema(self)
        # This supports logging the original value for attrs implemented in __setattr__ below
        self.__original_attrs__ = {}

        # Move class-defined attributes into a private var
        # Create regular properties holding values passed in via constructor
        for aname in dir(self):
            attr = getattr(self, aname)
            if isinstance(attr, (Enumeration, Constraint)):
                self.__class_attrs__[aname] = attr
                # TODO - use validate() from attr
                setattr(self, aname, kwargs.get(aname, None))
            if isinstance(attr, Column):
                self.__class_attrs__[aname] = attr
                # TODO - use validate() from attr
                setattr(self, aname, attr.ctype.instantiate(kwargs.get(aname, None)))

        # Set _pkid
        # Helpful for update and other maintenance tasks
        setattr(self, "_pkid", kwargs.get("_pkid", None))

    def __repr__(self):
        values = []
        for v in self.__schema__.column_names:
            values.append("{0}={1}".format(v, getattr(self, v, None)))
        return "{0}: {1}".format(self.__class__.__name__, ",".join(values))

    def __setattr__(self, key, value):
        """Capture original attribute values specified at instantiation before allowing them to be updated."""
        # This supports the ability to know what attributes
        # have changed in support of doing a vbr.update_row(object)
        try:
            current = getattr(self, key)
            if not isinstance(current, Column):
                if key not in self.__original_attrs__:
                    self.__original_attrs__[key] = current
        except Exception:
            pass
        super().__setattr__(key, value)

    def updates(self) -> dict:
        """Return a dict of attributes updated since instantation."""
        return self.__original_attrs__

    def clone(self):
        """Return a mutable clone of this VBR object."""
        return copy.deepcopy(self)

    def dict(self):
        """Return a dict filtered for use in row insert or update operations"""
        dct = {}
        for v in self.__schema__.column_names:
            _d = getattr(self, v, None)

            # Cast to proper Python type
            d = self.__class_attrs__[v].ctype.cast(_d)

            # Do not populate dict with None values where attribute is a primary key
            # Do not populate dict with None values if attribute is nullable
            nullable = self.__class_attrs__[v].nullable
            is_pk = self.__class_attrs__[v].primary_key
            if d is not None:
                dct[v] = d
            elif nullable is False and is_pk is False:
                dct[v] = d

        return dct

    def json(self, indent=0, sort_keys=True, class_name=None):
        # TODO - deal with datetime
        return json.dumps(
            self.dict(), indent=indent, sort_keys=sort_keys, cls=class_name
        )

    def primary_key_id(self):
        """Return value of VBR row primary key."""
        return getattr(self, "_pkid", None)


class AssociationTable(Table):
    __left__ = None
    __right__ = None
