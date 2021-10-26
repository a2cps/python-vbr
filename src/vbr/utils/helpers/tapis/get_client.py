from tapipy import actors
from .tapis_local_cache import TapisLocalCache

__all__ = ['get_client']


def get_client():
    try:
        # Works on local host
        return TapisLocalCache.restore()
    except Exception:
        # Works inside a Tapis Actor.
        return actors.get_client()
