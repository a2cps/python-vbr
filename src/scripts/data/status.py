from .loader import TableData


class StatusData(TableData):
    DATA = [{
        'status_id': 0,
        'name': 'redcap.incomplete',
        'description': 'REDcap event_status incomplete'
    }, {
        'status_id': 1,
        'name': 'redcap.partial',
        'description': 'REDcap event_status partially complete or unverified'
    }, {
        'status_id': 2,
        'name': 'redcap.complete',
        'description': 'REDcap event_status complete'
    },
    {
        'status_id': 10,
        'name': 'sample.collected',
        'description': 'Sample collected'
    },{
        'status_id': 11,
        'name': 'sample.frozen',
        'description': 'Sample frozen'
    },{
        'status_id': 12,
        'name': 'sample.thawed',
        'description': 'Sample thawed'
    },
    {
        'status_id': 13,
        'name': 'sample.retired',
        'description': 'Sample retired'
    },
    {
        'status_id': 14,
        'name': 'sample.depleted',
        'description': 'Sample depleted'
    },
    {
        'status_id': 20,
        'name': 'shipment.packaged',
        'description': 'Shipment packaged'
    },
    {
        'status_id': 21,
        'name': 'shipment.shipped',
        'description': 'Shipment shipped'
    },
    {
        'status_id': 22,
        'name': 'shipment.in_transit',
        'description': 'Shipment in transit'
    },
    {
        'status_id': 23,
        'name': 'shipment.delayed',
        'description': 'Shipment in transit'
    },
    {
        'status_id': 24,
        'name': 'shipment.arrived',
        'description': 'Shipment arrived'
    },
    {
        'status_id': 25,
        'name': 'shipment.recieved',
        'description': 'Shipment recieved'
    },
    {
        'status_id': 26,
        'name': 'shipment.validated',
        'description': 'Shipment validated'
    },
    {
        'status_id': 27,
        'name': 'shipment.failed_validation',
        'description': 'Shipment failed validation'
    },
    {
        'status_id': 28,
        'name': 'shipment.lost',
        'description': 'Shipment lost'
    }
    ]
