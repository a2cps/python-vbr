from typing import NoReturn, Any
from tapipy.tapis import Tapis, TapisResult

class DataManager(object):
    """Manages data in PgREST collections
    """
    def create(self, vbr_obj: Any) -> TapisResult:
        """Insert a VBR Record into the database
        """
        root_url = vbr_obj.__schema__.root_url
        resp = self.client.pgrest.create_in_collection(
            collection=root_url, data=vbr_obj.dict())
        # I am not sure I want to return a TapisResult
        return resp

    def retrieve(self, pk_value: str, table_name: str) -> Any:
        """Retrieve a VBR Record from the database by primary key and table name
        """
        pass

    def update(self, vbr_obj: Any) -> NoReturn:
        """Update a VBR Record in the database
        """
        pass

    def delete(self, vbr_obj: Any) -> NoReturn:
        """Delete a VBR Record from the database
        """
        pass
