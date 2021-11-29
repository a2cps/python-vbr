from .loader import TableData


class StatusData(TableData):
    DATA = [
        {
            "status_id": 0,
            "name": "redcap.incomplete",
            "description": "REDcap event_status incomplete",
        },
        {
            "status_id": 1,
            "name": "redcap.partial",
            "description": "REDcap event_status partially complete or unverified",
        },
        {
            "status_id": 2,
            "name": "redcap.complete",
            "description": "REDcap event_status complete",
        },
        {
            "status_id": 10,
            "name": "created",
            "description": "Item was created in the VBR",
        },
        {
            "status_id": 20,
            "name": "sample.shipped",
            "description": "Sample marked as shipped",
        },
        {
            "status_id": 21,
            "name": "sample.received",
            "description": "Sample receipt acknowleged",
        },
        {
            "status_id": 22,
            "name": "sample.lost",
            "description": "Sample marked as never received",
        },
        {
            "status_id": 30,
            "name": "easypost.pre_transit",
            "description": "Shipment dispatched to carrier",
        },
        {
            "status_id": 31,
            "name": "easypost.in_transit",
            "description": "Shipment in transit",
        },
        {
            "status_id": 32,
            "name": "easypost.out_for_delivery",
            "description": "Shipment out for delivery",
        },
        {
            "status_id": 34,
            "name": "easypost.delivered",
            "description": "Shipment Delivered",
        },
        {
            "status_id": 35,
            "name": "easypost.return_to_sender",
            "description": "Shipment returned to sender",
        },
        {
            "status_id": 36,
            "name": "easypost.failure",
            "description": "Shipment failure",
        },
        {
            "status_id": 37,
            "name": "easypost.unknown",
            "description": "Shipment status unknown",
        },
        {
            "status_id": 40,
            "name": "shipment.shipped",
            "description": "Shipment dispatched to carrier",
        },
        {
            "status_id": 41,
            "name": "shipment.received",
            "description": "Shipment marked as received",
        },
        {
            "status_id": 42,
            "name": "shipment.delayed",
            "description": "Shipment marked as delayed",
        },
        {
            "status_id": 43,
            "name": "shipment.lost",
            "description": "Shipment marked as lost/destroyed",
        },
        {
            "status_id": 45,
            "name": "shipment.created",
            "description": "Shipment created in the system",
        },
        {
            "status_id": 50,
            "name": "container.present",
            "description": "Container is present",
        },
        {
            "status_id": 51,
            "name": "container.damaged",
            "description": "Container is damaged",
        },
        {
            "status_id": 52,
            "name": "container.missing",
            "description": "Container is missing",
        },
        {
            "status_id": 53,
            "name": "container.lost",
            "description": "Container is lost",
        },
        {
            "status_id": 60,
            "name": "measurement.present",
            "description": "Measurement is present",
        },
        {
            "status_id": 61,
            "name": "measurement.spoiled",
            "description": "Measurement is spoiled",
        },
        {
            "status_id": 62,
            "name": "measurement.depleted",
            "description": "Measurement is depleted",
        },
        {
            "status_id": 63,
            "name": "measurement.lost",
            "description": "Measurement has been lost",
        },
        {
            "status_id": 64,
            "name": "measurement.inflight",
            "description": "Measurement is in transit or in process of being validated",
        },
    ]
