from .constants import *

__all__ = ["Statuses"]


class Statuses:
    # NOTE - this must be manually synced with src/scripts/data/status.py
    CREATED = 10
    SHIPPED = 40
    SHIPMENT_SHIPPED = 40
    SHIPMENT_RECEIVED = 41
    SHIPMENT_DELAYED = 42
    SHIPMENT_LOST = 43
