"""Represent hiearchical relationships between types.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = [
    "BiosampleInDataset",
    "MeasurementInCollection",
    "ContainerInShipment",
    "DatasetInProject",
    "FileInDataEvent",
    "FileInDataset",
    "SubjectInDataset",
]

# Not needed. Each Biosample is derived from exactly one subject
# and so can be mapped by biosample.subject -> subject.subject_id
# class BiosampleInSubject(AssociationTable):
#     """Maps biosamples to subjects."""

#     biosample_from_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
#     biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
#     subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class BiosampleInDataset(AssociationTable):
    """Maps biosamples to datasets."""

    biosample_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    biosample = Column(
        Integer, ForeignKey("biosample.biosample_id", event_action="CASCADE")
    )
    dataset = Column(Integer, ForeignKey("dataset.dataset_id", event_action="CASCADE"))


class MeasurementInCollection(AssociationTable):
    """Maps measurements to collections."""

    measurement_in_collection_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    measurement = Column(
        Integer, ForeignKey("measurement.measurement_id", event_action="CASCADE")
    )
    collection = Column(
        Integer, ForeignKey("collection.collection_id", event_action="CASCADE")
    )
    signature = Signature("measurement", "collection")


class ContainerInShipment(AssociationTable):
    """Maps containers inside other shipments."""

    container_in_shipment_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Constrained to be unique so that a container can only be directly inside ONE other shipment
    container = Column(
        Integer,
        ForeignKey("container.container_id", event_action="CASCADE"),
        unique=True,
    )
    shipment = Column(
        Integer, ForeignKey("shipment.shipment_id", event_action="CASCADE")
    )
    signature = Signature("container", "shipment")


class DatasetInProject(AssociationTable):
    """Maps datasets to their associated projects."""

    dataset_in_project_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    dataset = Column(Integer, ForeignKey("dataset.dataset_id", event_action="CASCADE"))
    project = Column(Integer, ForeignKey("project.project_id", event_action="CASCADE"))


class FileInDataEvent(AssociationTable):
    """Maps files to data events which create or alter them."""

    file_in_data_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey("file.file_id", event_action="CASCADE"))
    data_event = Column(
        Integer, ForeignKey("data_event.data_event_id", event_action="CASCADE")
    )


class FileInDataset(AssociationTable):
    """Maps files to dataset collections."""

    file_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey("file.file_id", event_action="CASCADE"))
    dataset = Column(Integer, ForeignKey("dataset.dataset_id", event_action="CASCADE"))


# Not needed. Each Measurement is derived from exactly one Biosample
# and so can be mapped by measurement.biosample -> biosample.biosample_id
# class MeasurementInBiosample(AssociationTable):
#     """Maps measurements to biosamples."""
#     measurement_in_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
#     measurement_id = Column(Integer, ForeignKey('measurement.measurement_id'))
#     biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))


class SubjectInDataset(AssociationTable):
    """Maps subjects to dataset collections."""

    subject_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))
    dataset_id = Column(Integer, ForeignKey("dataset.dataset_id"))
