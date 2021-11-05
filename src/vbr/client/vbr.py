from .api import ApiManager
from .connection import Connection
from .data import DataManager
from .manage import TableManager


class VBR(Connection, DataManager, TableManager, ApiManager):
    pass
