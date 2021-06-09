from typing import NoReturn, Any
from tapipy.tapis import TapisResult


class DataManager(object):
    """Manages data in PgREST collections
    """
    def create_from_dict(self, root_url: str,
                         record_dict: dict) -> TapisResult:
        """Create a PgREST record from a Python dictionary
        """
        resp = self.client.pgrest.create_in_collection(collection=root_url,
                                                       data=record_dict)
        return resp

    def create(self, vbr_obj: Any) -> TapisResult:
        """Create a PgREST record from a VBR Table instance
        """
        root_url = vbr_obj.__schema__.root_url
        return self.create_from_dict(root_url=root_url, data=vbr_obj.dict())

    def retrieve(self,
                 pk_value: str,
                 root_url=None,
                 table_name=None) -> TapisResult:
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
