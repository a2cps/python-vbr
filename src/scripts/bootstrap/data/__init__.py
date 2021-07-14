import inspect

from vbr.pgrest import table
from vbr.tableclasses import class_from_table

from .anatomy import AnatomyData
from .assay_type import AssayTypeData
from .biosample import BiosampleData
from .box_type import BoxTypeData
from .contact import ContactData
from .data_event import DataEventData
from .data_type import DataTypeData
from .dataset import DatasetData
from .file import FileData
from .file_format import FileFormatData
from .loader import TableData
from .location import LocationData
from .organization import OrganizationData
from .project import ProjectData
from .protocol import ProtocolData
from .reason import ReasonData
from .role import RoleData
from .status import StatusData
from .subject import SubjectData
from .unit import UnitData

#__all__ = ['data_loads']


def _classes():
    """Private: Return the list of table data classes via Python inspection
    """
    import inspect
    import sys
    classlist = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if TableData in obj.__bases__:
                # Filter out the spurious table named association_table that
                # we get from importing AssociationTable
                if obj.__name__ not in ('TableData'):
                    classlist.append(obj)
    return tuple(classlist)


def class_from_name(table_name: str) -> TableData:
    """Return table data class by table class name
    """
    for c in _classes():
        try:
            if c.__name__ == table_name:
                return c
        except Exception:
            pass


def data_classes(table_definitions: list):
    ordered = []
    for t in table_definitions:
        tdef_name = t['table_name']
        tdef_classname = class_from_table(t['table_name']).__name__
        cl = class_from_name(tdef_classname + 'Data')
        if cl is not None:
            ordered.append(cl)
    return ordered


def data_loads(table_definition: list):
    """Return dependency-ordered list of data objects to load
    """
    ordered = []
    oc = data_classes(table_definition)
    for c in oc:
        for rec in c().records:
            ordered.append(rec)
    return ordered
