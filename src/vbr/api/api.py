from re import T

from tapipy.tapis import Tapis

from vbr.client import VBR
from vbr.tableclasses import Table
from vbr.utils.helpers import get_client

from ..utils.helpers import get_client
from .biosample import BiosampleApi
from .collection import CollectionApi
from .container import ContainerApi
from .container_type import ContainerTypeApi
from .data_event import DataEventApi
from .hierarchy import ShipmentHierarchyApi
from .history import HistoryApi
from .location import LocationApi
from .logistics import LogisticsApi
from .manage_status import ManageStatusApi
from .measurement import MeasurementApi
from .organization import OrganizationApi
from .project import ProjectApi
from .redcap import RcapTableApi
from .shipment import ShipmentApi
from .status import StatusApi
from .subject import SubjectApi
from .sysevent import SysEventApi
from .tracking_id import ManageTrackingIdApi

__all__ = ["get_vbr_api_client", "VBR_Api"]


def get_vbr_api_client(tapis_client: Tapis = None) -> VBR:
    """Instantiate a VBR client."""
    if tapis_client is None:
        tapis_client = get_client()
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

    def _get_row_from_table_with_id(self, root_url: str, pkid: str):
        """Get a row from table root_url by primary key identifier"""
        search_key = root_url + "_id"
        query = {search_key: {"operator": "=", "value": pkid}}
        return self._get_row_from_table_with_query(root_url=root_url, query=query)

    def _get_row_from_table_with_local_id(self, root_url: str, local_id: str) -> Table:
        """Get a row from table root_url by local_id"""
        query = {"local_id": {"operator": "=", "value": local_id}}
        return self._get_row_from_table_with_query(root_url=root_url, query=query)

    def _get_row_from_table_with_tracking_id(
        self, root_url: str, tracking_id: str
    ) -> Table:
        """Get a row from table root_url by tracking_id"""
        query = {"tracking_id": {"operator": "=", "value": tracking_id}}
        return self._get_row_from_table_with_query(root_url=root_url, query=query)

    def _get_rows_from_table_with_query(self, root_url: str, query: dict) -> Table:
        """Get rows by table root_url and pgrest 'where' query"""
        resp = self.vbr_client.query_rows(root_url=root_url, query=query)
        if len(resp) == 0:
            raise ValueError("{0} does not match any {1}".format(query, root_url))
        else:
            return resp

    def _get_row_from_table_with_query(self, root_url: str, query: dict) -> Table:
        """Get a row by table root_url and pgrest 'where' query"""
        resp = self._get_rows_from_table_with_query(root_url, query)
        if len(resp) > 1:
            raise ValueError("{0} resolves to multiple {1}".format(query, root_url))
        else:
            return resp[0]


class VBR_Api(
    ApiBase,
    BiosampleApi,
    CollectionApi,
    ContainerApi,
    ContainerTypeApi,
    DataEventApi,
    LocationApi,
    MeasurementApi,
    OrganizationApi,
    ProjectApi,
    RcapTableApi,
    ShipmentApi,
    SubjectApi,
    StatusApi,
    SysEventApi,
    LogisticsApi,
    ManageTrackingIdApi,
    ManageStatusApi,
    HistoryApi,
    ShipmentHierarchyApi,
):
    pass
