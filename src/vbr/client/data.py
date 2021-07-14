from typing import NoReturn, Any
from tapipy.tapis import TapisResult


class DataManager(object):
    """Manages data in PgREST collections
    """
    def create_row_from_dict(self, root_url: str,
                             record_data: dict) -> TapisResult:
        """Create a PgREST record from a Python dictionary
        """
        resp = self.client.pgrest.create_in_collection(collection=root_url,
                                                       data=record_data)
        return resp

    def create_row(self, vbr_obj: Any) -> TapisResult:
        """Create a PgREST record from a VBR Table instance
        """
        root_url = vbr_obj.__schema__.root_url
        return self.create_row_from_dict(root_url=root_url,
                                         record_data=vbr_obj.dict())

    def retrieve_row(self,
                     pk_value: str,
                     root_url=None,
                     table_name=None,
                     query=None) -> TapisResult:
        """Retrieve a VBR Record from the database by primary key and table name
        """
        resp = self.client.pgrest.get_in_collection(collection=root_url,
                                                    item=pk_value)
        return resp

    def update_row(self, vbr_obj: Any) -> NoReturn:
        """Update a VBR Record in the database
        """
        pass

    def delete_row(self, vbr_obj: Any) -> NoReturn:
        """Delete a VBR Record from the database
        """
        pass

    def list_rows(self, root_url, limit=None, offset=None):
        """Lists rows
        """
        pass
