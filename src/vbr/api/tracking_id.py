"""Manage tracking ID of VBR objects"""
from vbr.tableclasses import (
    Biosample,
    Collection,
    Container,
    Measurement,
    Shipment,
    Subject,
    Table,
)

from .data_event import DataEventApi


class ManageTrackingIdApi(object):
    def _relabel_row(self, vbr_row: Table, new_tracking_id: str) -> Table:
        """Relabel a VBR object with a new tracking ID"""
        if getattr(vbr_row, "tracking_id", None) is None:
            raise ValueError(
                "Cannot relabel <%s> object", vbr_row.__schema__.table_name
            )
        original_tracking_id = vbr_row.tracking_id
        vbr_row.tracking_id = new_tracking_id
        vbr_row = self.vbr_client.update_row(vbr_row)
        DataEventApi.create_and_link(
            self,
            comment="Relabeled from original tracking ID {0}".format(
                original_tracking_id
            ),
            link_target=vbr_row,
        )
        return vbr_row

    def relabel_biosample(self, local_id: str, new_tracking_id: str) -> Biosample:
        """Update a Biosample tracking_id (by local_id)."""
        bsam = self.get_biosample_by_local_id(local_id)
        return self._relabel_row(bsam, new_tracking_id)

    def relabel_collection(self, local_id: str, new_tracking_id: str) -> Collection:
        """Update a Collection tracking_id (by local_id)."""
        cont = self.get_collection_by_local_id(local_id)
        return self._relabel_row(cont, new_tracking_id)

    def relabel_container(self, local_id: str, new_tracking_id: str) -> Container:
        """Update a Container tracking_id (by local_id)."""
        cont = self.get_container_by_local_id(local_id)
        return self._relabel_row(cont, new_tracking_id)

    def relabel_container_by_local_id(
        self, local_id: str, new_tracking_id: str
    ) -> Container:
        """Deprecated function name: Update a Container tracking_id (by local_id)."""
        return self.relabel_container(local_id, new_tracking_id)

    def relabel_measurement(self, local_id: str, new_tracking_id: str) -> Measurement:
        """Update a Measurement tracking_id (by local_id)."""
        meas = self.get_measurement_by_local_id(local_id)
        return self._relabel_row(meas, new_tracking_id)

    def relabel_shipment(self, local_id: str, new_tracking_id: str) -> Shipment:
        """Update a Shipment tracking_id (by local_id)."""
        ship = self.get_shipment_by_local_id(local_id)
        return self._relabel_row(ship, new_tracking_id)

    def relabel_subject(self, local_id: str, new_tracking_id: str) -> Subject:
        """Update a Subject tracking_id (by local_id)."""
        subj = self.get_subject_by_local_id(local_id)
        return self._relabel_row(subj, new_tracking_id)
