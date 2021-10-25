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
        'name': 'created',
        'description': 'Item was created in the VBR'
    }]
