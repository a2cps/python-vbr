from . import errors
from . import record
from . import unique_record

from .record import SESSION_FIELD


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
        if getattr(c, 'TABLE') == table_name:
            return c
    raise errors.TableNotSupported(
        '{0} is not currently supported by the VBR module'.format(table_name))


class BioSample(unique_record.VBRUniqueRecord):
    """VBR biosample
    """
    TABLE = 'biosample'
    PRIMARY_KEY = 'biosample_id'
    FIELDS = [('biosample_id_namespace', 'varchar', True),
              ('biosample_id', 'serial', True),
              ('project_id_namespace', 'varchar', True),
              ('project', 'integer', True), ('persistent_id', 'varchar', True),
              ('creation_time', 'timestamp', False),
              ('sample_type', 'integer', False), ('anatomy', 'integer', False),
              ('subject', 'varchar', False), ('protocol', 'integer', True),
              ('event_id', 'integer', True)]


class Contact(record.VBRRecord):
    """VBR contact
    """
    TABLE = 'contact'
    PRIMARY_KEY = 'contact_id'
    FIELDS = [('contact_id', 'serial', True), ('first_name', 'varchar', False),
              ('last_name', 'varchar', False), ('phone', 'varchar', False),
              ('organization', 'integer', True)]


class DataEvent(unique_record.VBRUniqueRecord):
    """VBR data_event
    """
    TABLE = 'data_event'
    PRIMARY_KEY = 'data_event_id'
    FIELDS = [('data_event_id', 'serial', True),
              ('protocol', 'integer', False), ('rank', 'integer', False),
              ('event_ts', 'timestamp', False),
              ('event_count', 'integer', False), ('subject', 'varchar', False),
              ('performed_by', 'integer', False), ('status', 'integer', False),
              ('reason', 'integer', False), ('dataset', 'integer', False)]


class Dataset(record.VBRRecord):
    """VBR dataset
    """
    TABLE = 'dataset'
    PRIMARY_KEY = 'dataset_id'
    FIELDS = [('dataset_id', 'serial', True), ('data_source', 'integer', True),
              ('title', 'varchar', False), ('description', 'varchar', False),
              ('contained_in', 'integer', False)]


class DatasetOrganization(record.VBRRecord):
    """VBR dataset_organization
    """
    TABLE = 'dataset_organization'
    PRIMARY_KEY = None
    FIELDS = [('dataset', 'integer', True), ('organization', 'integer', True),
              ('role', 'integer', True)]


class File(unique_record.VBRUniqueRecord):
    """VBR file
    """
    TABLE = 'file'
    PRIMARY_KEY = 'file_id'
    FIELDS = [('file_id_namespace', 'varchar', True),
              ('file_id', 'serial', True),
              ('project_id_namespace', 'varchar', False),
              ('project', 'integer', True), ('subject', 'varchar', False),
              ('permanent_id', 'varchar', False),
              ('creation_time', 'timestamp', False),
              ('size_in_bytes', 'integer', False),
              ('sha256', 'varchar', False), ('md5', 'varchar', False),
              ('filename', 'varchar', False),
              ('file_format', 'integer', False),
              ('information_type', 'integer', False)]


class FileFormat(record.VBRRecord):
    """VBR file_format
    """
    TABLE = 'file_format'
    PRIMARY_KEY = 'file_format_id'
    FIELDS = [('file_format_id', 'serial', True), ('name', 'varchar', False),
              ('description', 'varchar', False),
              ('synonyms', 'varchar', False)]


class InformationType(record.VBRRecord):
    """VBR information_type
    """
    TABLE = 'information_type'
    PRIMARY_KEY = 'information_type_id'
    FIELDS = [('information_type_id', 'serial', True),
              ('name', 'varchar', True), ('description', 'varchar', True),
              ('synonyms', 'varchar', False)]


class Location(record.VBRRecord):
    """VBR location
    """
    TABLE = 'location'
    PRIMARY_KEY = 'location_id'
    FIELDS = [('location_id', 'serial', True),
              ('location_name', 'varchar', False),
              ('address1', 'varchar', False), ('address2', 'varchar', False),
              ('address3', 'varchar', False), ('city', 'varchar', False),
              ('zip_or_postcode', 'varchar', False),
              ('state_province_country', 'varchar', False),
              ('organization', 'integer', True)]


class Organization(unique_record.VBRUniqueRecord):
    """VBR organization
    """
    TABLE = 'organization'
    PRIMARY_KEY = 'organization_id'
    FIELDS = [('organization_id', 'serial', True), ('url', 'varchar', True),
              ('name', 'varchar', True), ('description', 'varchar', True),
              ('synonyms', 'varchar', False)]


class Project(unique_record.VBRUniqueRecord):
    """VBR project
    """
    TABLE = 'project'
    PRIMARY_KEY = 'project_id'
    FIELDS = [('id_namespace', 'varchar', True),
              ('project_id', 'serial', True), ('project_id', 'varchar', False),
              ('creation_time', 'timestamp', False),
              ('abbreviation', 'varchar', False), ('name', 'varchar', False),
              ('description', 'varchar', False)]


class Protocol(record.VBRRecord):
    """VBR protocol
    """
    TABLE = 'protocol'
    PRIMARY_KEY = 'protocol_id'
    FIELDS = [('protocol_id', 'serial', True), ('name', 'varchar', False),
              ('description', 'varchar', False),
              ('contained_in', 'integer', False)]


class Reason(record.VBRRecord):
    """VBR reason
    """
    TABLE = 'reason'
    PRIMARY_KEY = 'reason_id'
    FIELDS = [('reason_id', 'serial', True), ('name', 'varchar', True),
              ('reason_description', 'varchar', True)]


class Status(record.VBRRecord):
    """VBR status
    """
    TABLE = 'status'
    PRIMARY_KEY = 'status_id'
    FIELDS = [('status_id', 'serial', True), ('name', 'varchar', True),
              ('status_description', 'varchar', True)]


class Subject(unique_record.VBRUniqueRecord):
    """VBR subject
    """
    TABLE = 'subject'
    PRIMARY_KEY = 'subject_id'
    FIELDS = [('subject_id', 'serial', True), ('name', 'varchar', True),
              ('subject_description', 'varchar', True)]
