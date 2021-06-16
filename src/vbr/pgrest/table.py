import json
import datetime

from .column import Column
from .constraints import Constraint
from .enums import Enumeration
from .schema import PgrestSchema
from .utils import datetime_to_isodate

__all__ = ['Table', 'AssociationTable']


class Table(object):
    """PgREST Table
    """
    __tablename__ = None
    __rooturl__ = None

    # TODO - support for generating create/update JSON for PgREST

    def __init__(self, table_id=None, **kwargs):

        self.__table_id__ = table_id
        self.__class_attrs__ = {}
        self.__schema__ = PgrestSchema(self)

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

    def __repr__(self):
        values = []
        for v in self.__schema__.column_names:
            values.append('{0}={1}'.format(v, getattr(self, v, None)))
        return '{0}: {1}'.format(self.__class__.__name__, ','.join(values))

    def dict(self):
        dct = {}
        for v in self.__schema__.column_names:
            d = getattr(self, v, None)
            # TODO - genericize this based on property types?
            if isinstance(d, datetime.datetime):
                d = datetime_to_isodate(d)
            dct[v] = d
        return dct

    def json(self, indent=0, sort_keys=True, class_name=None):
        # TODO - deal with datetime
        return json.dumps(self.dict(),
                          indent=indent,
                          sort_keys=sort_keys,
                          cls=class_name)


class AssociationTable(Table):
    __left__ = None
    __right__ = None
