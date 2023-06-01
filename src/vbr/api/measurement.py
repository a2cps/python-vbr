from re import M
from typing import List

from vbr.pgrest.time import timestamp
from vbr.tableclasses import Biosample, Container, Measurement
from vbr.utils import utc_time_in_seconds

from .data_event import DataEventApi

DEFAULT_VOLUME_ML = 0.5

__all__ = ["MeasurementApi"]


class MeasurementApi(object):
    def get_measurement(self, pkid: str) -> Measurement:
        """Retrieve a Measurement by primary identifier."""
        return self._get_row_from_table_with_id("measurement", pkid)

    def get_measurement_by_local_id(self, local_id: str) -> Measurement:
        """Retrieve a Measurement by local_id."""
        return self._get_row_from_table_with_local_id("measurement", local_id)

    def get_measurement_by_tracking_id(self, tracking_id: str) -> Measurement:
        """Retrieve a Measurement by tracking_id."""
        return self._get_row_from_table_with_tracking_id("measurement", tracking_id)

    def create_measurement(
        self,
        tracking_id: str,
        biosample_id: int,
        project_id: int,
        measurement_type_id: int,
        unit_id: int,
        container_id: int,
        status_id: int,
        volume: float = DEFAULT_VOLUME_ML,
        creation_timestr: str = None,
        redcap_repeat_instance: int = None,
    ) -> Measurement:
        """Create a new Measurement."""
        # TODO - data_event
        bs = Measurement(
            tracking_id=tracking_id,
            biosample=biosample_id,
            project=project_id,
            measurement_type=measurement_type_id,
            unit=unit_id,
            container=container_id,
            status=status_id,
            volume=volume,
            creation_time=creation_timestr,
            redcap_repeat_instance=redcap_repeat_instance,
        )
        try:
            return self.vbr_client.create_row(bs)[0]
        except Exception:
            raise

    def create_or_get_measurement_by_tracking_id(
        self,
        tracking_id: str,
        biosample_id: int,
        project_id: int,
        measurement_type_id: int,
        unit_id: int,
        container_id: int,
        status_id: int,
        volume: float,
        creation_timestr: str = None,
        redcap_repeat_instance: int = None,
    ) -> Measurement:
        """Create a Measurement or return existing with specified tracking_id."""
        try:
            return self.create_measurement(
                tracking_id,
                biosample_id,
                project_id,
                measurement_type_id,
                unit_id,
                container_id,
                status_id,
                volume,
                creation_timestr,
                redcap_repeat_instance
            )
        except Exception:
            return self.get_measurement_by_tracking_id(tracking_id)

    def set_volume(
        self, measurement: Measurement, volume: float, comment: str = None
    ) -> Measurement:
        """Set the volume for a Measurement."""
        if volume < 0.0:
            raise ValueError("Volume cannot be negative")
        measurement.volume = volume
        measurement = self.vbr_client.update_row(measurement)

        DataEventApi.create_and_link(
            self,
            status_id=68,
            comment=comment,
            link_target=measurement,
        )
        return measurement

    def partition_measurement(
        self,
        measurement: Measurement,
        volume: int,
        tracking_id: str = None,
        comment: str = None,
    ) -> Measurement:
        """Create a sub-Measuremenent from a Measurement."""

        # validate provided volume
        if measurement.volume < volume:
            raise ValueError(
                "Cannot partition volume of {0} from a volume of {1}".format(
                    volume, measurement.volume
                )
            )

        # 1. Clone the original Measurement to a new Measurement,
        m2 = measurement.clone()
        m2.volume = volume
        m2.measurement_id = None
        m2.local_id = None
        m2.creation_time = timestamp()
        # Append timestamp to extant tracking_id if one not provided
        if tracking_id is not None:
            m2.tracking_id = tracking_id
        else:
            m2.tracking_id = measurement.tracking_id + "." + utc_time_in_seconds()
        m2 = self.vbr_client.create_row(m2)[0]

        # Decrease the volume of original measurement
        new_parent_volume = measurement.volume - volume
        self.set_volume(measurement, new_parent_volume)

        # TODO Register the relation via MeasurementFromMeasurement table
        DataEventApi.create_and_link(
            self,
            comment="Partitioned to {0}".format(m2.local_id),
            link_target=measurement,
        )
        return m2

    def get_measurement_partitions(self, measurement: Measurement) -> List[Measurement]:
        """Retrieve Measurements partioned from a Measurment."""
        # Query MeasurementFromMeasurement table
        raise NotImplemented()

    def get_measurements_in_container(self, container: Container) -> List[Measurement]:
        """Retrieve Measurements in a Container."""
        query = {"container": {"operator": "=", "value": container.container_id}}
        return self.vbr_client.query_rows(
            root_url="measurement", query=query, limit=1000000
        )

    def get_measurements_in_biosample(self, biosample: Biosample, redcap_repeat_instance) -> List[Measurement]:
        """Retrieve Measurements in a Biosample."""
        # PgREST doesn't handle =None queries well, patch:
        if redcap_repeat_instance is not None:
            query = {
                    "biosample": {"operator": "=", "value": biosample.biosample_id},
                    "redcap_repeat_instance": {"operator": "=", "value": redcap_repeat_instance}
                    }
        else:
            query = {
                "biosample": {"operator": "=", "value": biosample.biosample_id}}
        return self.vbr_client.query_rows(
            root_url="measurement", query=query, limit=1000000
        )
