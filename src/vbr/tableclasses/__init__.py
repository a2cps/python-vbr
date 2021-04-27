from .single import *
from .linkages import *

def _classes():
    """Private: Return the list of tableclasses via Python inspection
    """
    import inspect
    import sys
    classlist = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            classlist.append(obj)
    return tuple(classlist)


def class_from_table(table_name: str) -> record.VBRRecord:
    """Look up and return VBR table class by table name
    """
    for c in _classes():
        try:
            if c.table_name() == table_name:
                return c
        except Exception:
            pass
    raise errors.TableNotSupported(
        '"{0}" is not currently supported by the VBR module'.format(table_name))

