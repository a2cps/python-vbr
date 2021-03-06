from functools import lru_cache

from vbr.hashable import picklecache

from .. import errors
from ..pgrest import AssociationTable, DependencySolver, Table
from .associations import *
from .vbr_table import TableVBR

# from .redcap.autogenerated import * # Importing * pulls in all tables but we are avoiding that during development
try:
    from .redcap.autogenerated import (
        RcapBloodSampleCollectionAndProcessingCrf,
        RcapConsentedParticipantInformation,
        RcapPatientDemographicsBaselineV03DemographicsI,
        RcapPatientDemographicsFullPart2V03Demographics,
    )
except ImportError:
    from .redcap.autogenerated import *

from .redcap.rcaptable import RcapTable
from .single_tables import *
from .system import *


@picklecache.mcache(lru_cache(maxsize=128))
def _classes():
    """Private: Return the list of tableclasses via Python inspection"""
    import inspect
    import sys

    classlist = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if (
                Table in obj.__bases__
                or TableVBR in obj.__bases__
                or AssociationTable in obj.__bases__
                or RcapTable in obj.__bases__
                or VbrSysEventTable in obj.__bases__
            ):
                # Filter out the spurious table named association_table that
                # we get from importing AssociationTable
                if obj.__name__ not in (
                    "Table",
                    "TableVBR",
                    "AssociationTable",
                    "RcapTable",
                    "VbrSysEventTable",
                ):
                    classlist.append(obj)
    return tuple(classlist)


@picklecache.mcache(lru_cache(maxsize=128))
def class_from_table(table_name: str) -> Table:
    """Return VBR table class by table name"""
    for c in _classes():
        try:
            if c().__schema__.table_name == table_name:
                return c
        except Exception:
            pass
    raise errors.TableNotSupported(
        '"{0}" is not currently supported by the VBR module'.format(table_name)
    )


@picklecache.mcache(lru_cache(maxsize=128))
def table_from_class(class_obj: type) -> str:
    """Return VBR table class by class"""
    return class_obj().__schema__.table_name


@picklecache.mcache(lru_cache(maxsize=128))
def table_from_classname(class_name: str) -> str:
    """Return VBR table class by class name"""
    pass


def table_definitions():
    defs = []
    classes = _classes()
    for c in classes:
        defs.append(c().__schema__.definition)
    defs = DependencySolver(defs).ordered_emit()
    return defs
