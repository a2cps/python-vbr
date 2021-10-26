from vbr.client import VBR
from vbr.utils.helpers import get_client
from vbr.tableclasses import Table
from .biosample import BiosampleApi
from .container import ContainerApi
from .data_event import DataEventApi
from .location import LocationApi
from .measurement import MeasurementApi
from .project import ProjectApi
from .redcap import RcapTableApi
from .shipment import ShipmentApi
from .subject import SubjectApi
# These must be imported after the table-specific Api classes
from .container_logistics import ContainerLogisticsApi
from .measurement_logistics import MeasurementLogisticsApi
from tapipy.tapis import Tapis

from functools import lru_cache
from vbr.hashable import picklecache

__all__ = ['get_vbr_api_client', 'VBR_Api']


def get_vbr_api_client(tapis_client: Tapis = None) -> VBR:
    """Instantiate a VBR client."""
    return VBR_Api(tapis_client=tapis_client)


class ApiBase(object):
    def __init__(self, tapis_client: Tapis = None):
        # If tapis client not provided try to bootstrap
        # from localhost and then environment vars. This
        # is an affordance to assist with local and
        # in-actor debugging
        if tapis_client is None:
            tapis_client = get_client()
        self.vbr_client = VBR(tapis_client)

    @picklecache.mcache(lru_cache(maxsize=32))
    def _get_row_from_table_with_id(self, root_url: str, pkid: str):
        """Get a row from table root_url by primary key identifier"""
        search_key = root_url + '_id'
        query = {search_key: {'operator': '=', 'value': pkid}}
        return self._get_row_from_table_with_query(root_url=root_url,
                                                   query=query)

    @picklecache.mcache(lru_cache(maxsize=32))
    def _get_row_from_table_with_local_id(self, root_url: str,
                                          local_id: str) -> Table:
        """Get a row from table root_url by local_id"""
        query = {'local_id': {'operator': '=', 'value': local_id}}
        return self._get_row_from_table_with_query(root_url=root_url,
                                                   query=query)

    @picklecache.mcache(lru_cache(maxsize=32))
    def _get_row_from_table_with_tracking_id(self, root_url: str,
                                             tracking_id: str) -> Table:
        """Get a row from table root_url by tracking_id"""
        query = {'tracking_id': {'operator': '=', 'value': tracking_id}}
        return self._get_row_from_table_with_query(root_url=root_url,
                                                   query=query)

    @picklecache.mcache(lru_cache(maxsize=32))
    def _get_row_from_table_with_query(self, root_url: str,
                                       query: dict) -> Table:
        """Get a row by table root_url and pgrest 'where' query"""
        resp = self.vbr_client.query_rows(root_url=root_url, query=query)
        if len(resp) > 1:
            raise ValueError('Resolves to multiple {0}'.format(root_url))
        elif len(resp) == 0:
            raise ValueError('Does not match any {0}'.format(root_url))
        else:
            return resp[0]


class VBR_Api(ApiBase, BiosampleApi, ContainerApi, DataEventApi, LocationApi,
              MeasurementApi, ProjectApi, RcapTableApi, ShipmentApi,
              SubjectApi, ContainerLogisticsApi, MeasurementLogisticsApi):
    pass
