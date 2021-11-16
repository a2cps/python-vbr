from .loader import TableData


class ProjectInProjectData(TableData):
    DATA = [
        {
            "project": 2,
            "parent_project": 1,
        },
        {
            "project": 3,
            "parent_project": 1,
        },
    ]
