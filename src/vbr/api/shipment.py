from vbr.tableclasses import Shipment

__all__ = ['ShipmentApi']


class ShipmentApi(object):
    def get_shipment(self, pkid: str) -> Shipment:
        """Retrieve a shipment by primary identifier."""
        return self._get_row_from_table_with_id('shipment', pkid)

    def get_shipment_by_local_id(self, local_id: str) -> Shipment:
        """Retrieve a shipment by local_id."""
        return self._get_row_from_table_with_local_id('shipment', local_id)

    def get_shipment_by_tracking_id(self, tracking_id: str) -> Shipment:
        """Retrieve a shipment by tracking_id."""
        return self._get_row_from_table_with_tracking_id(
            'shipment', tracking_id)

    def create_shipment(self, tracking_id: str, project_id: int, name: str,
                        sender_name: str, source_record_id: str,
                        ship_to_id: int, ship_from_id: int) -> Shipment:
        """Create a new Shipment."""
        sh = Shipment(tracking_id=tracking_id,
                      project=project_id,
                      name=name,
                      sender_name=sender_name,
                      source_record_id=source_record_id,
                      ship_to=ship_to_id,
                      ship_from=ship_from_id)
        try:
            return self.vbr_client.create_row(sh)[0]
        except Exception:
            raise

    def create_or_get_shipment_by_tracking_id(self, tracking_id: str,
                                              project_id: int, name: str,
                                              sender_name: str,
                                              source_record_id: str,
                                              ship_to_id: int,
                                              ship_from_id: int) -> Shipment:
        """Create a Shipment or return existing with specified tracking_id."""
        try:
            return self.create_shipment(tracking_id, project_id, name,
                                        sender_name, source_record_id,
                                        ship_to_id, ship_from_id)
        except Exception:
            return self.get_shipment_by_tracking_id(tracking_id)
