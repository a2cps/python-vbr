from ..pgrest import *
from .constants import Constants

__all__ = ["TableVBR"]


class TableVBR(Table):
    local_id = Constants.STRING_LOCALID_COLUMN
