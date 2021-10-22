from vbr.pgrest.constraints import Signature
from ..pgrest import *
from .constants import Constants


class Anatomy(Table):
    """C2M2-defined table: id is an UBERON CV term locating the origin of a biosample within the physiology of its subject."""
    anatomy_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(String,
                         nullable=True,
                         comments="Description of this anatomy object")
    id = Column(
        String,
        comments=
        "UBERON CV term used to locate the origin of a biosample within the physiology of its source."
    )
    name = Column(String,
                  nullable=True,
                  comments="Short name for this anatomy object")


class AssayType(Table):
    """C2M2-defined table: describes types of material that can be biosamples. id is an OBI CV Term ID"""
    assay_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String, comments="OBI CV term ID", unique=True)
    description = Column(String,
                         nullable=True,
                         comments="Description of the assay_type")
    name = Column(String,
                  nullable=True,
                  comments="Short name for the assay_type")


class Biosample(Table):
    """C2M2-defined table: each record uniquely identifies a biosample obtained from a subject"""
    biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    creation_time = Column(Date)
    # Source: Redcap
    # MUST be unique!
    tracking_id = Column(String,
                         comments='ID assigned to sample when collected',
                         unique=True)
    anatomy = Column(Integer, ForeignKey('anatomy.anatomy_id'))
    project = Column(Integer, ForeignKey('project.project_id'))
    subject = Column(Integer, ForeignKey('subject.subject_id'))


class Container(Table):
    """TACC defined extension: a generic container class"""
    container_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    # Source: Usually Redcap but might also be user or LIMS
    # MUST be unique!
    tracking_id = Column(String,
                         comments='Tracking ID assigned to container',
                         unique=True)
    container_type = Column(
        Integer,
        ForeignKey('container_type.container_type_id'),
    # 0 is default virtual container
        default=0)
    # Allowing null value permits Container location to be assigned after creation
    # But.. setting to 0 by default forces location to default "system" container
    #
    # ForeignKey event_action='RESTRICT' prevents deletion of a location that
    # holds Containers without relocating them first
    location = Column(Integer,
                      ForeignKey('location.location_id',
                                 event_action='RESTRICT'),
                      nullable=True,
                      default=0)
    # TODO - implement as ForeignKey('container.container_id') but first update pgrest.solver to address self-refererence case
    parent_container = Column(
        Integer,
        nullable=True,
    # 0 is the system base container
        default=0,
        comments="Parent container_id. Permits nesting relationships.")


class ContainerType(Table):
    """Definitions for storage, shipping, and other containers"""
    container_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(String, nullable=True, comments="Descriptive name")
    name = Column(String,
                  unique=True,
                  comments="Short label (ex. 'aliquot' or 'paxgene'")


class Contact(Table):
    """TACC-defined table: contains administrative contact information"""
    contact_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    email = Column(String,
                   unique=True,
                   comments="Email address for notifications")
    first_name = Column(String, comments="First name")
    last_name = Column(String, comments="Last name")
    phone = Column(String,
                   nullable=True,
                   comments="Phone number for notifications (optional)")
    organization = Column(Integer,
                          ForeignKey('organization.organization_id'),
                          comments="Organization ID")


class DataEvent(Table):
    """C2M2 proposed future extension: logs data events with associated status, issues and comments."""

    data_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    event_ts = Column(CreatedTimeStamp, nullable=True)
    rank = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)
    performed_by = Column(Integer,
                          ForeignKey('contact.contact_id'),
                          nullable=True)
    protocol = Column(Integer,
                      ForeignKey('protocol.protocol_id'),
                      nullable=True)
    reason = Column(Integer, ForeignKey('reason.reason_id'), nullable=True)
    status = Column(Integer, ForeignKey('status.status_id'), nullable=True)
    # Enforces record uniqueness. Signature is just syntactic sugar for
    # defining a UniqueConstraint
    # signature = Signature('protocol', 'rank', 'event_ts', 'performed_by',
    #   'status', 'reason')


class Dataset(Table):
    """C2M2-defined table: a named collection of files and other datasets."""
    # Within a2cps, an initial dataset will be created for each subject and protocol (event_type) to mirror the data collected via REDCap."""
    # Additional datasets may be created and mapped using dataset mapping tables to reflect commonly queried cross-sections of data with their associated files."""
    dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    tracking_id = Constants.STRING_PERSISTENT_ID
    abbreviation = Column(String,
                          nullable=True,
                          comments='Short display name for the dataset')
    creation_time = Column(CreatedTimeStamp,
                           comments='When the dataset was created',
                           nullable=True)
    description = Column(Text,
                         nullable=True,
                         comments='Description of the dataset')
    name = Column(String,
                  nullable=True,
                  comments='Short descriptive name for the dataset')


class DataType(Table):
    """C2M2-defined table: provides classifications for data; id is an EDAM CV data term in the form of data:[EDAM#]"""
    data_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String, comments='EDAM CV data term “data:[EDAM#]”')
    description = Column(Text,
                         comments='Description of the data_type',
                         nullable=True)
    name = Column(String, comments='Short name for this data_type')
    # Enforce unique combination of id and name
    signature = Signature('id', 'name')


class File(Table):
    """C2M2-defined table: provide unique persistent name and associated information for files"""
    file_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    project = Column(Integer, ForeignKey('project.project_id'))
    tracking_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp,
                           nullable=True,
                           comments="When the file was created")
    size_in_bytes = Column(Integer, nullable=True)
    uncompressed_size_in_bytes = Column(Integer, nullable=True)
    sha256 = Column(String)
    md5 = Column(String)
    # TODO - determine root level for filenames
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
    # TODO - set a default
    mime_type = Column(String, nullable=True)
    # TODO - determine what fields form the signature
    signature = Signature('filename', 'sha256', 'md5', 'size_in_bytes')


class FileFormat(Table):
    """C2M2-defined table containing classifications for file format. id is an EDAM CV format term."""
    file_format_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    id = Column(String, unique=True, comments='EDAM CV format: term')
    description = Column(Text, nullable=True)
    name = Column(String, nullable=True)


class Location(Table):
    """TACC-defined table: contains physical address information for shipping."""
    location_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    # Must be unique - this is display name
    display_name = Column(String, nullable=False, unique=True)

    address1 = Column(String, nullable=True)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_or_postcode = Column(String, nullable=True)
    state_province_country = Column(String, nullable=True)
    # Nullable to allow for addresses not mapped to a VBR organization
    organization = Column(Integer,
                          ForeignKey('organization.organization_id'),
                          nullable=True)


class Measurement(Table):
    """TACC-defined extension: contains sub-divisions of a biosample."""
    measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN

    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Currently cannot be unique in case tracking_id are reused
    tracking_id = Column(
        String, comments='Identifier assigned to measurement at creation')

    measurement_type = Column(
        Integer, ForeignKey('measurement_type.measurement_type_id'))
    unit = Column(Integer, ForeignKey('unit.unit_id'))

    biosample = Column(Integer, ForeignKey('biosample.biosample_id'))
    # Optional. Allows physical Measurement assets to be associated with a physical Container
    container = Column(Integer,
                       ForeignKey('container.container_id'),
                       nullable=True)
    project = Column(Integer, ForeignKey('project.project_id'))
    # Not sure this belongs here unless other core entities have a status field
    status = Column(Integer, ForeignKey('status.status_id'))


class MeasurementType(Table):
    """Definitions for types of measurement"""
    measurement_type_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(String, nullable=True, comments="Descriptive name")
    name = Column(String,
                  unique=True,
                  comments="Short label (ex. 'plasma' or 'paxgene'")


class Organization(Table):
    """C2M2 proposed future extension: a list of data-generating research programs or entities."""
    organization_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    name = Column(String)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True)
    signature = Signature('url', 'name')


class Project(Table):
    """C2M2-defined table uniquely defining projects within the scope of the VBR and broader NIH namespace."""
    project_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    abbreviation = Column(String, nullable=True)
    creation_time = Column(CreatedTimeStamp, nullable=True)
    description = Column(Text, nullable=True)
    name = Column(String, unique=True)
    tracking_id = Constants.STRING_PERSISTENT_ID


class Protocol(Table):
    """C2M2 proposed future extension: an event-type or defined process."""
    protocol_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(Text, nullable=True)
    name = Column(String, nullable=False)
    tracking_id = Column(String, nullable=True)


class Reason(Table):
    """TACC-defined table of reasons for incomplete status to aid analysis of participant dropouts, biosample QA, logistics, and other issues."""
    reason_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(Text)
    name = Column(String, unique=True)


class Role(Table):
    """TACC-defined table: defines permissions associated with users of this system."""
    role_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    description = Column(Text)
    name = Column(String)
    url = Column(String)
    # TODO - confirm these fields
    signature = Signature('url', 'name')


class Shipment(Table):
    """Provides details for shipping biosamples"""
    shipment_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    tracking_id = Column(String,
                         unique=True,
                         comments="Fedex or UPS shipment tracking barcode")
    # e.g. Shipment from Rush 10/18/2021
    name = Column(String, nullable=True, comments="Free text name of shipment")
    # e.g. mcc
    # shipment_notes = Column(String, nullable=True, comments="Free text description of shipment")
    # e.g. Bill Miller
    sender_name = Column(String,
                         nullable=True,
                         comments="Free text name of sender")
    # e.g. 31-5
    source_record_id = Column(String,
                              nullable=True,
                              comments='REDCap record_id for shipment')
    # Shipment 
    project = Column(Integer, ForeignKey('project.project_id'))
    ship_to = Column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    # Default is mtaub@jhsph.edu
    ship_from = Column(Integer,
                       ForeignKey("contact.contact_id"),
                       default=6,
                       nullable=True)
    status = Column(Integer, ForeignKey('status.status_id'))


class Status(Table):
    """TACC-defined table; status_id mirrors the REDCap 0 (incomplete), 1 (partial), and 2 (complete) status with extensibility for additional status definitions."""
    status_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    name = Column(String, unique=True)
    description = Column(Text)


class Subject(Table):
    """The source organism(s) from which a biosample has been generated."""
    subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    local_id = Constants.STRING_LOCALID_COLUMN
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Is this a candidate for use of PgREST enumerations?
    granularity = Column(String,
                         default='cfde_subject_granularity:0',
                         nullable=True)
    source_subject_id = Column(
        String,
        comments='REDCap record_id or EHRR case reference',
        unique=False,
        identifier=True)
    # A subject's persistent ID is the GUID assigned by REDcap
    tracking_id = Column(String,
                         comments='GUID assigned to subject',
                         unique=True)
    project = Column(Integer, ForeignKey('project.project_id'))


class Unit(Table):
    """Physical unit for measurements"""
    unit_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    name = Column(
        String,
        unique=True,
        nullable=False,
        comment=
        "Short label for unit (ex. '1ml_tube', 'microscope_slide' or 'tissue_punch'"
    )
    description = Column(String,
                         comment="Short descriptive name used for the unit ")
