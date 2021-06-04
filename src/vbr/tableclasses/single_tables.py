from .pgrest import *

PROJECT_NAMESPACE = 'tag:a2cps.org'


class Anatomy(Table):
    anatomy_id = Column(Serial, primary_key=True)
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


class AssayType(Table):
    assay_type_id = Column(Serial, primary_key=True)
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


class Biosample(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    bs_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    biosample_id = Column(Serial, primary_key=True)
    project_id_namesapace = Column(String, default=PROJECT_NAMESPACE)
    project_local_id = Column(String)
    bs_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namesapace', 'project_local_id')
    project = Column(Integer, ForeignKey('project.project_id'))
    persistent_id = Column(String)
    creation_time = Column(DateTime)
    anatomy = Column(Integer, ForeignKey('anatomy.anatomy_id'))


class BiosampleFromSubject(Table):
    biosample_from_subject_id = Column(Serial, primary_key=True)
    biosample_id_namespace = Column(String, default=PROJECT_NAMESPACE)
    biosample_local_id = Column(String)
    bsfs_biosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    # TODO - what is the default here?
    subject_id_namespace = Column(String, default=PROJECT_NAMESPACE)
    subject_local_id = Column(String)
    bsfs_subject_id_namespace_subject_local_id = UniqueConstraint(
        'subject_id_namespace', 'subject_local_id')
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class BiosampleInDataset(Table):
    biosample_in_dataset_id = Column(Serial, primary_key=True)
    biosample_id_namespace = Column(String, default=PROJECT_NAMESPACE)
    biosample_local_id = Column(String)
    bsid_biosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    dataset_id_namespace = Column(String, default=PROJECT_NAMESPACE)
    dataset_local_id = Column(String)
    bsid_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'dataset_id_namespace', 'dataset_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class Contact(Table):
    contact_id = Column(Serial, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    organization = Column(Integer, ForeignKey('organization.organization_id'))


class DataEvent(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    de_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    data_event_id = Column(Serial, primary_key=True)
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


# TODO - a bunch of linkage tables


class Dataset(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    ds_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    dataset_id = Column(Serial, primary_key=True)
    persistent_id = Column(String)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    abbreviation = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class DatasetDefinedByProject(Table):
    pass


class DatasetInDataset(Table):
    pass


class DataType(Table):
    data_type_id = Column(Serial, primary_key=True)
    id = Column(String)
    name = Column(String)
    description = Column(Text)


class File(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    fl_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    file_id = Column(Serial, primary_key=True)
    project_id_namesapace = Column(String, default=PROJECT_NAMESPACE)
    project_local_id = Column(String)
    fl_project_id_namespace_project_local_id = UniqueConstraint(
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


class FileDescribesBiosample(Table):
    pass


class FileDescribesSubject(Table):
    pass


class FileFormat(Table):
    file_format_id = Column(Serial, primary_key=True)
    id = Column(String)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class FileInDataEvent(Table):
    pass


class FileInDataset(Table):
    pass


class FileInFile(Table):
    pass


class Location(Table):
    location_id = Column(Serial, primary_key=True)
    location_name = Column(String, nullable=True)
    address1 = Column(String, nullable=True)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_or_postcode = Column(String, nullable=True)
    state_province_country = Column(String, nullable=True)
    organization = Column(Integer, ForeignKey('organization.organization_id'))


class Organization(Table):
    organization_id = Column(Serial, primary_key=True)
    url = Column(String)
    name = Column(String)
    description = Column(Text)


class Project(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    pr_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    project_id = Column(Serial, primary_key=True)
    persistent_id = Column(String, nullable=True)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    abbreviation = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class Protocol(Table):
    protocol_id = Column(Serial, primary_key=True)
    id = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)


class ProtocolInProtocol(Table):
    pass


class Reason(Table):
    reason_id = Column(Serial, primary_key=True)
    name = Column(String)
    reason_description = Column(Text)


class Role(Table):
    role_id = Column(Serial, primary_key=True)
    url = Column(String)
    name = Column(String)
    description = Column(Text)


class Status(Table):
    status_id = Column(Serial, primary_key=True)
    name = Column(String)
    status_description = Column(Text)


class Subject(Table):
    id_namespace = Column(String, default=PROJECT_NAMESPACE)
    local_id = Column(String)
    sb_id_namespace_local_id = UniqueConstraint('id_namespace', 'local_id')
    subject_id = Column(Serial, primary_key=True)
    project_id_namesapace = Column(String, default=PROJECT_NAMESPACE)
    project_local_id = Column(String)
    sb_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namesapace', 'project_local_id')
    project = Column(Integer, ForeignKey('project.project_id'))
    persistent_id = Column(String, nullable=True)
    creation_time = Column(DateTime, nullable=True, default='CREATETIME')
    granularity = Column(String, nullable=True)


class SubjectInDataset(Table):
    pass
