from .. import errors
from . import record
from .pgrest import Table, DependencySolver
from .single_tables import *
from .linkage_tables import *


def _classes():
    """Private: Return the list of tableclasses via Python inspection
    """
    import inspect
    import sys
    classlist = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if Table in obj.__bases__:
                classlist.append(obj)
    return tuple(classlist)


def class_from_table(table_name: str) -> Table:
    """Return VBR table class by table name
    """
    for c in _classes():
        try:
            if c().__schema__.table_name == table_name:
                return c
        except Exception:
            pass
    raise errors.TableNotSupported(
        '"{0}" is not currently supported by the VBR module'.format(
            table_name))


def table_from_class(class_obj: type) -> str:
    """Return VBR table class by class
    """
    return class_obj().__schema__.table_name


def table_from_classname(class_name: str) -> str:
    """Return VBR table class by class name
    """
    pass


def table_definitions():
    defs = []
    classes = _classes()
    for c in classes:
        defs.append(c().__schema__.definition)
    defs = DependencySolver(defs).ordered_emit()
    return defs
