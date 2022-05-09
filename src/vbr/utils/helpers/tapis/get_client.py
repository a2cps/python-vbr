import os

import tapipy
from tapipy import errors, tapis

from .tapis_local_cache import TapisLocalCache

__all__ = ["get_client"]


def actors_get_client():
    """Returns a pre-authenticated Tapis client using the abaco environment variables."""
    # if we have an access token, use that:
    if os.environ.get("_abaco_access_token"):
        tp = tapis.Tapis(
            base_url=os.environ.get("_abaco_api_server").strip('/'),
            access_token=os.environ.get("_abaco_access_token"),
        )
    elif os.environ.get("_abaco_api_server"):
        # otherwise, create a client with a fake JWT. this will only work if the actor is supplying its
        # own token to itself via a config object or the message, etc.
        tp = tapis.Tapis(base_url=os.environ.get("_abaco_api_server").strip('/'), jwt="123")
    else:
        raise errors.BaseTapyException(
            "Unable to instantiate a Tapis client: no token found."
        )
    return tp


def get_client():
    """Return a configured Tapis client from environment"""
    try:
        # Works inside a Tapis Actor.
        return actors_get_client()
    except errors.BaseTapyException:
        # Works on configured local host
        t = TapisLocalCache.restore()
        t.get_tokens()
        return t
    except Exception:
        raise
