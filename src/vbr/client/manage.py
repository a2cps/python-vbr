from typing import NoReturn, Any
from tapipy.tapis import Tapis, TapisResult

__all__ = ['TableManager']

class TableManager(object):
    """Manages PgREST tables
    """
    def create_table(self, table_object: Any) -> NoReturn:
        tdef = table_object.__schema__.definition()
        resp = self.client.pgrest.create_table(**tdef)
        return resp

    def update_table(self, table_object: Any) -> NoReturn:
        pass

    def delete_table(self, table_id) -> NoReturn:
        pass

    def list_tables(self) -> list:
        pass

    def get_table(self, table_identifier) -> NoReturn:
        pass
