from .loader import TableData


class StatusData(TableData):
    DATA = [{
        'status_id': 0,
        'name': 'incomplete',
        'description': 'incomplete'
    }, {
        'status_id': 1,
        'name': 'partial',
        'description': 'partially complete or unverified'
    }, {
        'status_id': 2,
        'name': 'complete',
        'description': 'complete'
    }]
