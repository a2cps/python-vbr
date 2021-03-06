from typing import Any, NoReturn

from tapipy.tapis import Tapis, TapisResult

from vbr.pgrest import table

from .connection import TapisDirectClient

__all__ = ["TableManager"]


class TableManager(object):
    """Manage PgREST tables"""

    def create_table_from_definition(self, table_def: dict) -> NoReturn:
        """Create a new PgREST table from a table dictionary (if authorized)"""
        # Disable use of Tapipy for this until OAPI spec is updated to include constraints
        # resp = self.client.pgrest.create_table(**table_def)
        #
        # Use TapisDirectClient instead to make a POST
        direct_client = TapisDirectClient(self.client)
        direct_client.setup("pgrest", api_path="manage/tables")
        resp = direct_client.post(json=table_def)
        return resp

    def create_table(self, table_object: Any) -> NoReturn:
        """Create a PgREST table from a VBR Table (if authorized)"""
        tdef = table_object.__schema__.definition()
        resp = self.create_table_from_definition(tdef)
        return resp

    def update_table(self, table_object: Any, table_id: int) -> NoReturn:
        """Update a PgREST table with with a VBR Table (if authorized)"""
        # TODO - back out the str(table_id) since tapipy should be able to handle an int
        raise NotImplementedError("Table updates are not yet supported")

    def delete_table(self, table_id: int) -> bool:
        """Delete a PgREST table by id (if authorized)"""
        # TODO - back out the str(table_id) since tapipy should be able to handle an int
        resp = self.client.pgrest.delete_table(table_id=str(table_id))
        return resp

    def list_tables(self) -> list:
        """List PgREST tables (if authorized)"""
        resp = self.client.pgrest.list_tables()
        tables = []
        for r in resp:
            tables.append(
                {
                    "table_id": r.get("table_id"),
                    "table_name": r.get("table_name"),
                    "root_url": r.get("root_url"),
                    "primary_key": r.get("primary_key"),
                }
            )
        return tables

    def get_table(self, table_id: int, details: bool = True) -> TapisResult:
        """Return a PgREST tables by id (if authorized)"""
        # TODO - back out the str(table_id) since tapipy should be able to handle an int
        resp = self.client.pgrest.get_manage_table(table_id=str(table_id), details=True)
        return resp
