from functools import lru_cache
from typing import Any, NoReturn, Dict, List

from tapipy.tapis import TapisResult

from vbr.client.connection import TapisDirectClient
from vbr.hashable import picklecache
from vbr.tableclasses import Table, class_from_table, vbr_table


class DataManager(object):
    """Manages data in PgREST collections"""

    @picklecache.mcache(lru_cache(maxsize=128))
    def _table_root_or_name_to_root(self, table_name=None, root_url=None) -> str:
        if root_url is not None:
            return root_url
        else:
            tables = self.pgrest.list_tables()
            for t in tables:
                if t.get("table_name") == table_name:
                    return t.get("root_url")
            raise ValueError(
                "Failed to resolve table with name == {0}".format(table_name)
            )

    @picklecache.mcache(lru_cache(maxsize=128))
    def _tapis_result_to_vbr(self, tres: TapisResult, root_url: str) -> Table:
        cl = class_from_table(root_url)
        return cl(**tres.__dict__)

    @picklecache.mcache(lru_cache(maxsize=128))
    def _dict_result_to_vbr(self, dres: dict, root_url: str) -> Table:
        cl = class_from_table(root_url)
        return cl(**dres)

    def create_row_from_dict(self, root_url: str, record_data: dict) -> Table:
        """Create a PgREST record from a Python dictionary"""
        resp = self.client.pgrest.add_table_row(root_url=root_url, data=record_data)
        if isinstance(resp, list):
            return [self._tapis_result_to_vbr(r, root_url) for r in resp]
        else:
            return self._tapis_result_to_vbr(resp, root_url)
        return resp

    def create_row(self, vbr_obj: Table) -> Table:
        """Create a PgREST record from a VBR Table instance"""
        root_url = vbr_obj.__schema__.root_url
        data_dict = vbr_obj.dict()
        return self.create_row_from_dict(root_url=root_url, record_data=data_dict)

    def retrieve_row(
        self,
        pk_value: str,
        root_url: str = None,
        table_name: str = None,
        query: str = None,
    ) -> Table:
        """Retrieve a VBR Record from the database by primary key and table name"""
        # TODO - support either root_url or table_name
        # TODO - support query
        pk_value = str(pk_value)
        resp = self.client.pgrest.get_table_row(root_url=root_url, item=pk_value)[0]
        if isinstance(resp, list):
            return [self._tapis_result_to_vbr(r, root_url) for r in resp]
        else:
            return self._tapis_result_to_vbr(resp, root_url)
        return resp

    def update_row(self, vbr_obj: Table) -> Table:
        """Update a VBR Record in the database."""
        # Valid _pkid probably signifies means object was created by Class(**row_dict)
        # assert vbr_obj._pkid is not None,
        #     'VBR object is not derived from a VBR database record. Create it first before updating it.'

        root_url = vbr_obj.__schema__.root_url
        pk_value = getattr(vbr_obj, "._pkid", None)
        if pk_value is None:
            pk_attr_name = vbr_obj.__schema__.table_name + "_id"
            pk_value = getattr(vbr_obj, pk_attr_name)
        pk_value = str(pk_value)

        # Assemble differences into an update payload
        payload = {}
        for k, v in vbr_obj.updates().items():
            # Get new value for k
            # TODO - only do this if new and old values are different
            payload[k] = getattr(vbr_obj, k)

        # Only attempt the update if the payload is not empty.
        # Otherwise, pgrest throws an error.
        # TODO - report this as an issue with pgrest
        if len(payload.items()) > 0:
            payload = {"data": payload}
            resp = self.client.pgrest.update_table_row(
                root_url=root_url, item=pk_value, request_body=payload
            )[0]
            return self._tapis_result_to_vbr(resp, root_url)
        else:
            # No change, return original VBR object
            # I think this is the right thing to do.
            return vbr_obj

    def delete_row(
        self, vbr_obj: Table, root_url: str = None, pk_value: str = None
    ) -> NoReturn:
        """Delete a VBR Record from the database."""
        # delete_table_row
        # Use either details from VBR object OR passed parameters to
        # specify which row to delete
        if vbr_obj._pkid is not None:
            pk_value = str(vbr_obj._pkid)
            root_url = vbr_obj.__schema__.root_url
        else:
            pk_value = str(pk_value)
            root_url = str(root_url)
        # assert pk_value is not None, 'Either a fully-formed VBR object or root_url and pk_value parameters must be provided.'
        self.client.pgrest.delete_table_row(root_url=root_url, item=pk_value)
        # Mark the VBR object as not being attached to a real record
        vbr_obj._pkid = None
        # No return!

    def list_rows(self, root_url: str, limit: int = 100000, offset: int = 0) -> list:
        """Lists VBR Records in table"""
        resp = self.client.pgrest.get_table_rows(
            root_url=root_url, limit=limit, offset=offset
        )

        rows = [self._tapis_result_to_vbr(tr, root_url) for tr in resp]
        return rows

    def _query_to_where_params(self, query: dict, param_els=None) -> list:
        # Tranform query, expressed as a where dict, into a
        # list of where parameters. MAPPINGS exists to support
        # code written against the older version of the pgrest API
        MAPPINGS = {"operators": {"=": "eq"}}
        if isinstance(param_els, list):
            elements = param_els
        else:
            elements = []
        if isinstance(query, dict):
            for k, v in query.items():
                # Default to equality operator
                op_orig = v.get("operator", "eq")
                operator = MAPPINGS["operators"].get(op_orig, op_orig)
                elements.append("{0}.{1}={2}".format(k, operator, v.get("value")))
        return elements

    def _build_url_params(
        self, query: Dict, limit: int = 1000000, offset: int = 0
    ) -> str:
        url_params = ""
        # Limit, Offset, and Where are implemented in the pgrest
        # API as URL parameters. These are bundled into a list
        # param_els then appended to the table data API URL
        param_els = []
        # Limit and offset
        if limit is not None:
            param_els.append("limit={}".format(limit))
        if offset is not None:
            param_els.append("offset={}".format(offset))
        # Transform
        param_els = self._query_to_where_params(query, param_els)
        # Extend api_path with where parameter
        if len(param_els) > 0:
            url_params = "?" + "&".join(param_els)
        return url_params

    def query_rows(
        self, root_url: str, query: Dict = None, limit: int = 100000, offset: int = 0
    ) -> List[Table]:
        """Query a VBR Table for Records."""
        # Set up direct HTTP API client because tapipy does not
        # yet support pgrest where constructs
        client = TapisDirectClient(self.client)
        client.setup(service_name="pgrest", api_path="data")
        api_path = root_url
        url_params = self._build_url_params(query, limit, offset)
        api_path = api_path + url_params

        # Perform and return the API call
        resp = client.get(path=api_path)
        rows = []
        for r in resp:
            rows.append(self._dict_result_to_vbr(r, root_url))
        return rows

    def query_view_rows(
        self, view_name: str, query: Dict = None, limit: int = 100000, offset: int = 0
    ) -> List[Dict]:
        """Query a view."""
        # Returns a dict because we don't necessarily have schema models for
        # custom views
        #
        # Set up direct HTTP API client because tapipy does not
        # yet support pgrest where constructs
        client = TapisDirectClient(self.client)
        client.setup(service_name="pgrest", api_path="views")
        api_path = view_name
        url_params = self._build_url_params(query, limit, offset)
        api_path = api_path + url_params
        # Perform and return the API call
        resp = client.get(path=api_path)
        rows = []
        for r in resp:
            # Response from Tapis is a list of Python dicts
            rows.append(r)
        return rows
