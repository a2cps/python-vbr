import tapipy
from tapipy.actors import actors
from .tapis_local_cache import TapisLocalCache

__all__ = ['get_client']


def get_client():
    try:
        # Works inside a Tapis Actor.
        return actors.get_client()
    except tapipy.errors.BaseTapyException:
        # Works on configured local host
        return TapisLocalCache.restore()
    except Exception:
        raise
