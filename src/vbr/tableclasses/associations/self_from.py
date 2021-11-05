"""Represent descendant relationships for the same type.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = ["MeasurementFromMeasurement", "FileFromFile"]


class MeasurementFromMeasurement(AssociationTable):
    """Maps measurements derived from another measurement."""

    measurement_from_measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Constrained: A measurement can only be derived from one source
    measurement = Column(
        Integer,
        ForeignKey("measurement.measurement_id", event_action="CASCADE"),
        unique=True,
    )
    source_measurement = Column(
        Integer, ForeignKey("container.container_id", event_action="CASCADE")
    )


class FileFromFile(AssociationTable):
    """Maps files derived from other files."""

    file_from_file_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Not constrained: Allow a file to be derived from multiple source files
    file = Column(Integer, ForeignKey("file.file_id", event_action="CASCADE"))
    source_file = Column(Integer, ForeignKey("file.file_id", event_action="CASCADE"))
