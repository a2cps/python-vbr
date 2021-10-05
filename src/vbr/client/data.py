from typing import NoReturn, Any
from tapipy.tapis import TapisResult
from vbr.tableclasses import class_from_table


class DataManager(object):
    """Manages data in PgREST collections
    """
    def _table_root_or_name_to_root(self, table_name=None, root_url=None):
        if root_url is not None:
            return root_url
        else:
            tables = self.pgrest.list_tables()
            for t in tables:
                if t.get('table_name') == table_name:
                    return t.get('root_url')
            raise ValueError(
                'Failed to resolve table with name == {0}'.format(table_name))

    def _tapis_result_to_vbr(self, tres: TapisResult, root_url: str) -> object:
        cl = class_from_table(root_url)
        return cl(**tres.__dict__)

    def create_row_from_dict(self, root_url: str,
                             record_data: dict) -> TapisResult:
        """Create a PgREST record from a Python dictionary
        """
        resp = self.client.pgrest.add_table_row(collection=root_url,
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
                     root_url: str = None,
                     table_name: str = None,
                     query: str = None) -> TapisResult:
        """Retrieve a VBR Record from the database by primary key and table name
        """
        # TODO - support either root_url or table_name
        # TODO - support query
        resp = self.client.pgrest.get_table_row(collection=root_url,
                                                item=pk_value)
        return self._tapis_result_to_vbr(resp, root_url)

    def update_row(self, vbr_obj: Any) -> NoReturn:
        """Update a VBR Record in the database
        """
        # update_table_row
        pass

    def delete_row(self, vbr_obj: Any) -> NoReturn:
        """Delete a VBR Record from the database
        """
        # delete_table_row
        pass

    def list_rows(self, root_url, limit=None, offset=None) -> TapisResult:
        """Lists VBR Records in table
        """
        resp = self.client.pgrest.get_table(collection=root_url,
                                            limit=limit,
                                            offset=offset)

        rows = [self._tapis_result_to_vbr(tr, root_url) for tr in resp]
        return rows
