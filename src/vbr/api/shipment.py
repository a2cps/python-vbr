from vbr.tableclasses import Shipment
from .data_event import DataEventApi
from .status import StatusApi

__all__ = ["ShipmentApi"]


class ShipmentApi(object):
    def get_shipment(self, pkid: str) -> Shipment:
        """Retrieve a shipment by primary identifier."""
        return self._get_row_from_table_with_id("shipment", pkid)

    def get_shipment_by_local_id(self, local_id: str) -> Shipment:
        """Retrieve a shipment by local_id."""
        return self._get_row_from_table_with_local_id("shipment", local_id)

    def get_shipment_by_tracking_id(self, tracking_id: str) -> Shipment:
        """Retrieve a shipment by tracking_id."""
        return self._get_row_from_table_with_tracking_id("shipment", tracking_id)

    def create_shipment(
        self,
        tracking_id: str,
        project_id: int,
        name: str,
        sender_name: str,
        source_record_id: str,
        ship_to_id: int,
        ship_from_id: int,
        status_id: int,
    ) -> Shipment:
        """Create a new Shipment."""
        sh = Shipment(
            tracking_id=tracking_id,
            project=project_id,
            name=name,
            sender_name=sender_name,
            source_record_id=source_record_id,
            ship_to=ship_to_id,
            ship_from=ship_from_id,
            status=status_id,
        )
        try:
            return self.vbr_client.create_row(sh)[0]
        except Exception:
            raise

    def create_or_get_shipment_by_tracking_id(
        self,
        tracking_id: str,
        project_id: int,
        name: str,
        sender_name: str,
        source_record_id: str,
        ship_to_id: int,
        ship_from_id: int,
        status_id: int,
    ) -> Shipment:
        """Create a Shipment or return existing with specified tracking_id."""
        try:
            return self.create_shipment(
                tracking_id,
                project_id,
                name,
                sender_name,
                source_record_id,
                ship_to_id,
                ship_from_id,
                status_id,
            )
        except Exception:
            return self.get_shipment_by_tracking_id(tracking_id)

    def update_shipment_status(
        self, shipment: Shipment, status: str, comment: str = None
    ) -> Shipment:
        status = status.upper()
        if status not in [
            "SHIPMENT_SHIPPED",
            "SHIPMENT_RECEIVED",
            "SHIPMENT_DELAYED",
            "SHIPMENT_LOST",
        ]:
            raise ValueError("Uknown value for shipment status %s", status)
        status_name = status.lower()
        status_name = status_name.replace("_", ".")
        vbr_status = StatusApi.get_status_by_name(self, status_name)
        shipment.status = vbr_status.primary_key_id()
        shipment = self.vbr_client.update_row(shipment)
        # DataEvent
        DataEventApi.create_and_link(
            self,
            status_id=vbr_status.primary_key_id(),
            comment=comment,
            link_target=shipment,
        )
        return shipment

    def relabel_shipment(self, local_id: str, new_tracking_id: str) -> Shipment:
        """Update the tracking_id for shipment by local_id."""
        # 1. Query for row matching local_id
        # 2. Set the new value
        # 3. Do database update via vbr_client.update_row()
        # 4. TODO Create and link a 'rename' data_event
        ship = self.get_shipment_by_local_id(local_id)
        ship.tracking_id = new_tracking_id
        ship = self.vbr_client.update_row(ship)
        return ship
