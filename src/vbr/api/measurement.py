from vbr.tableclasses import Measurement

from .data_event import DataEventApi
from .status import StatusApi

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
        creation_timestr: str = None,
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
            creation_time=creation_timestr,
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
        creation_timestr: str = None,
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
                creation_timestr,
            )
        except Exception:
            return self.get_measurement_by_tracking_id(tracking_id)

    def relabel_measurement(self, local_id: str, new_tracking_id: str) -> Measurement:
        """Update the tracking_id for measurement by local_id."""
        # 1. Query for row matching local_id
        # 2. Set the new value
        # 3. Do database update via vbr_client.update_row()
        meas = self.get_measurement_by_local_id(local_id)
        original_tracking_id = meas.tracking_id
        meas.tracking_id = new_tracking_id
        meas = self.vbr_client.update_row(meas)
        DataEventApi.create_and_link(
            self,
            comment="Relabeled from original tracking ID {0}".format(
                original_tracking_id
            ),
            link_target=meas,
        )
        return meas

    def update_measurement_status(
        self, measurement: Measurement, status: str, comment: str = None
    ) -> Measurement:
        """Update Measurement status by status name"""
        status = status.upper()
        if status not in [
            "MEASUREMENT_PRESENT",
            "MEASUREMENT_SPOILED",
            "MEASUREMENT_DEPLETED",
            "MEASUREMENT_LOST",
        ]:
            raise ValueError("Uknown value for measurement status %s", status)
        status_name = status.lower()
        status_name = status_name.replace("_", ".")
        vbr_status = StatusApi.get_status_by_name(self, status_name)
        measurement.status = vbr_status.primary_key_id()
        measurement = self.vbr_client.update_row(measurement)
        # DataEvent
        DataEventApi.create_and_link(
            self,
            status_id=vbr_status.primary_key_id(),
            comment=comment,
            link_target=measurement,
        )
        return measurement
