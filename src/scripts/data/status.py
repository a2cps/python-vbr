from .loader import TableData


class StatusData(TableData):
    DATA = [{
        'status_id': 0,
        'name': 'redcap.incomplete',
        'description': 'REDcap event_status incomplete'
    }, {
        'status_id':
        1,
        'name':
        'redcap.partial',
        'description':
        'REDcap event_status partially complete or unverified'
    }, {
        'status_id': 2,
        'name': 'redcap.complete',
        'description': 'REDcap event_status complete'
    }, {
        'status_id': 10,
        'name': 'liquid_sample.collected',
        'description': 'Liquid sample collected'
    }, {
        'status_id': 11,
        'name': 'liquid_sample.frozen',
        'description': 'Liquid sample frozen'
    }, {
        'status_id': 12,
        'name': 'liquid_sample.thawed',
        'description': 'Liquid sample thawed'
    }, {
        'status_id': 13,
        'name': 'liquid_sample.retired',
        'description': 'Liquid sample retired'
    }, {
        'status_id': 14,
        'name': 'liquid_sample.depleted',
        'description': 'Liquid sample depleted'
    }, {
        'status_id': 20,
        'name': 'shipment.packaged',
        'description': 'Shipment packaged'
    }, {
        'status_id': 21,
        'name': 'shipment.shipped',
        'description': 'Shipment accepted by carrier'
    }, {
        'status_id': 22,
        'name': 'shipment.in_transit',
        'description': 'Shipment in transit via carrier'
    }, {
        'status_id': 23,
        'name': 'shipment.delayed',
        'description': 'Shipment delayed by carrier'
    }, {
        'status_id': 24,
        'name': 'shipment.delivered',
        'description': 'Shipment delivered by carrier'
    }, {
        'status_id': 25,
        'name': 'shipment.recieved',
        'description': 'Shipment recieved by project personnel'
    }, {
        'status_id': 26,
        'name': 'shipment.validated',
        'description': 'Shipment contents validated'
    }, {
        'status_id': 27,
        'name': 'shipment.failed_validation',
        'description': 'Shipment failed validation'
    }, {
        'status_id': 28,
        'name': 'shipment.destroyed',
        'description': 'Shipment lost in transit'
    }]
