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

    def create_table_from_definition(self, table_definition: dict) -> NoReturn:
        resp = self.client.pgrest.create_table(**table_definition)
        return resp

    def update_table(self, table_object: Any) -> NoReturn:
        pass

    def delete_table(self, table_id) -> NoReturn:
        pass

    def list_tables(self) -> list:
        resp = self.client.pgrest.list_tables()
        tables = []
        for r in resp:
            tables.append(
                {
                    'table_id': r.get('table_id'),
                    'table_name': r.get('table_name'),
                    'root_url': r.get('root_url'),
                    'primary_key': r.get('primary_key')
                }
            )
        return tables

    def get_table(self, table_identifier) -> NoReturn:
        pass
