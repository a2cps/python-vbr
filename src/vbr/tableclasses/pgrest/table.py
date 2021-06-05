from .column import Column
from .constraints import Constraint
from .enums import Enumeration
from .schema import PgrestSchema

__all__ = ['Table', 'RelationTable']


class Table(object):
    """PgREST Table
    """
    __tablename__ = None
    __rooturl__ = None

    # TODO - support for generating create/update JSON for PgREST

    def __init__(self, **kwargs):

        self.__class_attrs__ = {}
        self.__schema__ = PgrestSchema(self)

        # Move class-defined attributes into a private var
        # Create regular properties holding values passed in via constructor
        for aname in dir(self):
            attr = getattr(self, aname)
            if isinstance(attr, (Column, Enumeration, Constraint)):
                self.__class_attrs__[aname] = attr
                # TODO - use validate() from attr
                setattr(self, aname, kwargs.get(aname, None))


class RelationTable(Table):
    __parent__ = None
    __child__ = None
