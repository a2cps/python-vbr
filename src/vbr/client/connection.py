"""VBR Database Driver
"""
import logging
import os
import uuid
from typing import NoReturn, Any

from tapipy.tapis import Tapis, TapisResult

# from . import constants, errors
# from .tableclasses import (SESSION_FIELD, class_from_linkage, class_from_table,
#                            record, unique_record)

logging.basicConfig(level=logging.DEBUG)

__all__ = ['Connection']


class Connection(object):
    """Provides a PgREST client
    """
    def __init__(self, tapis_client: Tapis, session=None, auto_connect=True):

        if session is None:
            self.session = uuid.uuid4().hex
        else:
            self.session = str(session)
        logging.debug('VBR Session: ' + self.session)

        self.client = tapis_client
        if auto_connect:
            self.connect()

    def connect(self, tapis_client: Tapis = None) -> NoReturn:
        if tapis_client is not None:
            self.client = tapis_client
        self.client.get_tokens()



# NOTE - One idea is to implement left/right relations in the connection class.
#        For example, do a retrieve on an object, then inspect to see if it has
#        any relations. If so, retrieve the related object and attach it to
#        the current one as a named property.  This would be done recursively
#        through the related object tree. Rendering to a dict/JSON for
#        consumption/usage would be recursive as well. We would not directly
#        support updates. Deletes should be supported implicitly via built-in
#        foreign key on_delete behavior.
