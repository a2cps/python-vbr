from .. import errors
from . import record
from .single_tables import *
from .linkage_tables import *
from .record import SESSION_FIELD


def _classes():
    """Private: Return the list of tableclasses via Python inspection
    """
    import inspect
    import sys
    classlist = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            classlist.append(obj)
    return tuple(classlist)


def class_from_table(table_name: str) -> record.VBRRecord:
    """Return VBR table class by table name
    """
    for c in _classes():
        try:
            if c.table_name() == table_name:
                return c
        except Exception:
            pass
    raise errors.TableNotSupported(
        '"{0}" is not currently supported by the VBR module'.format(
            table_name))


def class_from_linkage(child_table_name: str,
                       parent_table_name: str) -> record.VBRRecord:
    """Return VBR linkage class by child and parent table names
    """
    for c in _classes():
        try:
            if c.parent() == parent_table_name and c.child(
            ) == child_table_name:
                return c
        except Exception:
            pass
    raise errors.LinkageNotSupported(
        'Linking "{0}" => "{1}" is not currently supported by the VBR module'.
        format(child_table_name, parent_table_name))
