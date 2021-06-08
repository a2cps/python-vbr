from vbr.pgrest.constraints import Signature
from ..pgrest import *
from .constants import Constants


class Anatomy(Table):
    """C2M2-defined table: id is an UBERON CV term locating the origin of a biosample within the physiology of its subject."""
    anatomy_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


class AssayType(Table):
    """C2M2-defined table: describes types of material that can be biosamples. id is an OBI CV Term ID"""
    assay_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


class Biosample(Table):
    """C2M2-defined table: each record uniquely identifies a biosample obtained from a subject"""
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id_namesapace = Constants.STRING_NAMESPACE_COLUMN
    project_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namesapace', 'project_local_id')
    project = Column(Integer, ForeignKey('project.project_id'))
    persistent_id = Column(String)
    creation_time = Column(DateTime)
    anatomy = Column(Integer, ForeignKey('anatomy.anatomy_id'))


class Contact(Table):
    """TACC-defined table: contains administrative contact information"""
    contact_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    organization = Column(Integer, ForeignKey('organization.organization_id'))


class DataEvent(Table):
    """C2M2 proposed future extension: logs data events with associated status, issues and comments."""   
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    data_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    protocol = Column(Integer,
                      ForeignKey('protocol.protocol_id'),
                      nullable=True)
    rank = Column(Integer, nullable=True)
    event_ts = Column(DateTime, nullable=True, default='CREATETIME')
    performed_by = Column(Integer,
                          ForeignKey('contact.contact_id'),
                          nullable=True)
    status = Column(Integer, ForeignKey('status.status_id'), nullable=True)
    reason = Column(Integer, ForeignKey('reason.reason_id'), nullable=True)
    comment = Column(String)

    signature = Signature()


class Dataset(Table):
    """C2M2-defined table: a named collection of files and other datasets."""
    """Within a2cps, an initial dataset will be created for each subject and protocol (event_type) to mirror the data collected via REDCap."""
    """Additional datasets may be created and mapped using dataset mapping tables to reflect commonly queried cross-sections of data with their associated files."""
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    persistent_id = Column(String)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    abbreviation = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class DataType(Table):
    """C2M2-defined table: provides classifications for data; id is an EDAM CV data term in the form of data:[EDAM#]"""
    data_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String)
    name = Column(String)
    description = Column(Text)


class File(Table):
    """C2M2-defined table: provide unique persistent name and associated information for files"""
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    file_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id_namesapace = Constants.STRING_NAMESPACE_COLUMN
    project_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namesapace', 'project_local_id')
    project = Column(Integer, ForeignKey('project.project_id'))
    persistent_id = Column(String)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    size_in_bytes = Column(Integer, nullable=True)
    uncompressed_size_in_bytes = Column(Integer, nullable=True)
    sha256 = Column(String)
    md5 = Column(String)
    filename = Column(String)
    file_format = Column(Integer,
                         ForeignKey('file_format.file_format_id'),
                         nullable=True)
    data_type = Column(Integer,
                       ForeignKey('data_type.data_type_id'),
                       nullable=True)
    assay_type = Column(Integer,
                        ForeignKey('assay_type.assay_type_id'),
                        nullable=True)
    mime_type = Column(String, nullable=True)


class FileFormat(Table):
    """C2M2-defined table containing classifications for file format. id is an EDAM CV format term."""  
    file_format_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class Location(Table):
    """TACC-defined table: contains physical address information for shipping."""
    location_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    location_name = Column(String, nullable=True)
    address1 = Column(String, nullable=True)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_or_postcode = Column(String, nullable=True)
    state_province_country = Column(String, nullable=True)
    organization = Column(Integer, ForeignKey('organization.organization_id'))


class Organization(Table):
    """C2M2 proposed future extension: a list of data-generating research programs or entities."""
    organization_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    url = Column(String)
    name = Column(String)
    description = Column(Text)


class Project(Table):
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    project_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    persistent_id = Column(String, nullable=True)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    abbreviation = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class Protocol(Table):
    protocol_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class Reason(Table):
    reason_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    name = Column(String)
    description = Column(Text)


class Role(Table):
    """Defines permissions associated with users of this system."""
    role_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    url = Column(String)
    name = Column(String)
    description = Column(Text)


class Status(Table):
    status_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    name = Column(String)
    description = Column(Text)


class Subject(Table):
    """The source organism(s) from which a biosample has been generated."""
    id_namespace = Constants.STRING_NAMESPACE_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    uniq_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id_namesapace = Constants.STRING_NAMESPACE_COLUMN
    project_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namesapace', 'project_local_id')
    project_id = Column(Integer, ForeignKey('project.project_id'))
    persistent_id = Column(String, nullable=True)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    # Is this a candidate for use of PgREST enumerations?
    granularity = Column(String, nullable=True)
