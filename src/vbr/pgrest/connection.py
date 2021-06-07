"""VBR Database Driver
"""
import logging
import os
import uuid
from typing import NoReturn, Any

from tapipy.tapis import Tapis

# from . import constants, errors
# from .tableclasses import (SESSION_FIELD, class_from_linkage, class_from_table,
#                            record, unique_record)

logging.basicConfig(level=logging.DEBUG)

__all__ = ['VBRConn']


class VBRConn(object):
    def __init__(self, tapis_client: Tapis, session=None, auto_connect=True):

        if session is None:
            self.session = uuid.uuid4().hex
        else:
            self.session = str(session)
        logging.debug('VBR Session: ' + self.session)

        self.client = tapis_client
        if auto_connect:
            self.connect()

    def connect(self, tapis_client: Tapis = None):
        if tapis_client is not None:
            self.client = tapis_client
        self.client.get_tokens()

    def create(self, vbr_object: Any) -> str:
        """Insert a VBR Record into the database
        """
        pass

    def retrieve(self, pk_value: str, table_name: str) -> Any:
        """Retrieve a VBR Record from the database by primary key and table name
        """
        pass

    def update(self, vbr_object: Any) -> NoReturn:
        """Update a VBR Record in the database
        """
        pass

    def delete(self, vbr_object: Any) -> NoReturn:
        """Delete a VBR Record from the database
        """
        pass


# NOTE - One idea is to implement left/right relations in the connection class.
#        For example, do a retrieve on an object, then inspect to see if it has
#        any relations. If so, retrieve the related object and attach it to
#        the current one as a named property.  This would be done recursively
#        through the related object tree. Rendering to a dict/JSON for
#        consumption/usage would be recursive as well. We would not directly
#        support updates. Deletes should be supported implicitly via built-in
#        foreign key on_delete behavior.

    def create_table(self, table_object: Any) -> NoReturn:
        tdef = table_object.__schema__.definition()
        resp = self.client.pgrest.create_table(**tdef)
        return resp.get('table_id')

    def update_table(self, table_object: Any) -> NoReturn:
        pass

    def delete_table(self, table_id) -> NoReturn:
        pass

    def list_tables(self) -> list:
        pass

    def get_table(self, table_identifier) -> NoReturn:
        pass
