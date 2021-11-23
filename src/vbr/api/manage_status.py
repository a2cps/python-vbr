"""Manage status of VBR objects"""
from vbr.tableclasses import Container, Measurement, Shipment, Status, Table

from .data_event import DataEventApi
from .status import StatusApi

__all__ = ["ManageStatusApi"]


class ManageStatusApi(object):
    def _status_from_status_name(self, status_name: str, table_name: str) -> Status:
        """Returns a Status for a valid status and table name."""
        status_name = status_name.lower()
        status_prefix = table_name + "."
        if not status_name.startswith(status_prefix):
            status_name = status_prefix + status_name
        try:
            return StatusApi.get_status_by_name(self, status_name)
        except ValueError:
            raise ValueError("Unrecognized %s status %s", table_name, status_name)

    def _update_row_status(
        self, vbr_row: Table, status: Status, comment: str = None
    ) -> Table:
        """Update a VBR row with the provided Status"""
        if getattr(vbr_row, "status", None) is None:
            raise ValueError(
                "Cannot update status of <%s> object", vbr_row.__schema__.table_name
            )
        new_status_id = status.status_id
        ori_status_id = vbr_row.status
        if new_status_id != ori_status_id:
            vbr_row.status = new_status_id
        vbr_row = self.vbr_client.update_row(vbr_row)
        DataEventApi.create_and_link(
            self,
            status_id=new_status_id,
            comment=comment,
            link_target=vbr_row,
        )
        return vbr_row

    def update_container_status_by_name(
        self, container: Container, status_name: str, comment: str = None
    ) -> Container:
        """Update Container status by status.name"""
        new_status = self._status_from_status_name(status_name, "container")
        return self._update_row_status(container, new_status, comment)

    def update_measurement_status_by_name(
        self, measurement: Measurement, status_name: str, comment: str = None
    ) -> Measurement:
        """Update Measurement status by status.name"""
        new_status = self._status_from_status_name(status_name, "measurement")
        return self._update_row_status(measurement, new_status, comment)

    def update_shipment_status_by_name(
        self, shipment: Shipment, status_name: str, comment: str = None
    ) -> Shipment:
        """Update Shipment status by status.name"""
        new_status = self._status_from_status_name(status_name, "shipment")
        return self._update_row_status(shipment, new_status, comment)

    def _get_vbr_row_status(self, vbr_row: Table) -> Status:
        """Get Status for the provided VBR row."""
        if getattr(vbr_row, "status", None) is None:
            raise ValueError(
                "Cannot get status of <%s> object", vbr_row.__schema__.table_name
            )
        return StatusApi.get_status(self, vbr_row.status)

    def get_container_status(self, container: Container) -> Status:
        """Get current Status for a Container."""
        return self._get_vbr_row_status(container)

    def get_measurement_status(self, measurement: Measurement) -> Status:
        """Get current Status for a Measurement."""
        return self._get_vbr_row_status(measurement)

    def get_shipment_status(self, shipment: Shipment) -> Status:
        """Get current Status for a Shipment."""
        return self._get_vbr_row_status(shipment)
