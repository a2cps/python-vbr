from . import record
from . import class_from_linkage

def linkage_record_from_vbr_objects(child: record.VBRRecord, parent: record.VBRRecord) -> record.VBRRecord:
    """Instantiate a linkage record from two VBR objects
    """
    table_class = class_from_linkage(child.table_name(), parent.table_name())
    constructor_params = {
        table_class.primary_key(): None,
        child.primary_key(): child.get_field(child.primary_key()),
        parent.primary_key(): parent.get_field(parent.primary_key())
    }
    table_class_instance = table_class(**constructor_params)
    return table_class_instance
