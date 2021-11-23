from typing import List

from vbr.tableclasses import Container, DataEvent, Measurement, Shipment

from .data_event import DataEventApi


class HistoryApi(object):
    def get_container_history(self, container: Container) -> List[DataEvent]:
        """Get all DataEvents for a Container."""
        return DataEventApi.data_events_for_record(self, record=container)

    def get_measurement_history(self, measurement: Measurement) -> List[DataEvent]:
        """Get all DataEvents for a Measurement."""
        return DataEventApi.data_events_for_record(self, record=measurement)

    def get_shipment_history(self, shipment: Shipment) -> List[DataEvent]:
        """Get all DataEvents for a Shipment."""
        return DataEventApi.data_events_for_record(self, record=shipment)
