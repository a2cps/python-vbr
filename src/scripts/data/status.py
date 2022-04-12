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
            "description": "Item was created",
        },
        {
            "status_id": 11,
            "name": "present",
            "description": "Item is present",
        },
        {
            "status_id": 12,
            "name": "absent",
            "description": "Item is missing or lost",
        },
        {
            "status_id": 13,
            "name": "deleted",
            "description": "Item was deleted or destroyed",
        },
        {
            "status_id": 20,
            "name": "biosample.created",
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
            "status_id": 46,
            "name": "shipment.processed",
            "description": "Shipment processed after being received.",
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
            "status_id": 54,
            "name": "container.created",
            "description": "Container was created",
        },
        {
            "status_id": 55,
            "name": "container.destroyed",
            "description": "Container was destroyed",
        },
        {
            "status_id": 60,
            "name": "measurement.present",
            "description": "Item is present",
        },
        {
            "status_id": 61,
            "name": "measurement.spoiled",
            "description": "Item is spoiled",
        },
        {
            "status_id": 62,
            "name": "measurement.depleted",
            "description": "Item is depleted",
        },
        {
            "status_id": 63,
            "name": "measurement.lost",
            "description": "Item is lost",
        },
        {
            "status_id": 64,
            "name": "measurement.inflight",
            "description": "Item is in transit or in process of being validated",
        },
        {
            "status_id": 65,
            "name": "measurement.destroyed",
            "description": "Item was destroyed",
        },
        {
            "status_id": 66,
            "name": "measurement.inuse",
            "description": "Item is actively in use",
        },
        {
            "status_id": 67,
            "name": "measurement.available",
            "description": "Item is avaiable for use",
        },
        {
            "status_id": 68,
            "name": "measurement.changed_volume",
            "description": "Item volume was changed",
        },
        {
            "status_id": 70,
            "name": "sysevent.created",
            "description": "Event created by system",
        },
        {
            "status_id": 71,
            "name": "sysevent.received",
            "description": "Event received into system",
        },
        {
            "status_id": 72,
            "name": "sysevent.processing",
            "description": "Event is being processed by the system",
        },
        {
            "status_id": 73,
            "name": "sysevent.processing_complete",
            "description": "Event was processed by the system.",
        },
        {
            "status_id": 74,
            "name": "sysevent.processing_failed",
            "description": "Event was unable to be processed by the system.",
        },
        {
            "status_id": 80,
            "name": "collection.ready",
            "description": "Collection is ready for use.",
        },
        {
            "status_id": 81,
            "name": "collection.processing",
            "description": "Collection is being processed.",
        },
        {
            "status_id": 82,
            "name": "collection.processed",
            "description": "Collection has been processed.",
        },
    ]
