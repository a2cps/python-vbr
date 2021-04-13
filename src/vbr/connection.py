"""VBR Database Driver
"""
import psycopg2
import logging
import os
import uuid
from typing import NoReturn

from . import constants
from . import errors
from . import record
from . import tableclasses

logging.basicConfig(level=logging.DEBUG)


class VBRConn:
    """Managed connection to a VBR PostgreSQL database
    """

    CONNECT_TIMEOUT = 30

    def __init__(self, config:dict=None, session:str=None, no_connect:bool=False):
        if session is None:
            self.session = uuid.uuid4().hex
        else:
            self.session = str(session)
        logging.debug('VBR Session: ' + self.session)
        if no_connect is False:
            self.db = self._connect(config)
        else:
            self.db = None

    def _connect(self, config:dict=None) -> NoReturn:

        # Environment variables and defaults supported by the VBR database driver
        cfg = [('VBR_HOST', 'ip', 'localhost'),
               ('VBR_USERNAME', 'user', 'vbruser'),
               ('VBR_PASSWORD', 'pass', None), ('VBR_DATABASE', 'db', 'vbr')]

        if config == None:
            config = {}
        vbr = {}
        for env_var, cfg_key, default in cfg:
            vbr[cfg_key] = config.pop(cfg_key, os.getenv(env_var, None))

        logging.debug('Connecting to database {} on {}'.format(
            vbr['db'], vbr['ip']))
        conn = psycopg2.connect(host=vbr['ip'],
                                database=vbr['db'],
                                user=vbr['user'],
                                password=vbr['pass'],
                                connect_timeout=self.CONNECT_TIMEOUT)
        logging.debug('(Connected)')

        return conn

    def retrieve_record(self, pk_value:str, table_name:str) -> record.VBRRecord:
        """Retrieve a VBR Record from the database by primary key and table name
        """

        # Get SQL attributes and data from VBR Record
        rec_cls = tableclasses.class_from_table(table_name)
        db_table = rec_cls.TABLE
        db_pk = rec_cls.PRIMARY_KEY
        db_cols = rec_cls.field_names(include_pk=True)
        sql_columns = ','.join(db_cols)

        # Fetch record from database
        # Resolve class C for record
        # Return C(**record)
        SQL = "SELECT {} FROM {} WHERE {} = %s LIMIT 1".format(
            sql_columns, db_table, db_pk)
        conn = self.db
        with conn:
            with conn.cursor() as cur:
                logging.debug(cur.mogrify(SQL, [pk_value,]))
                cur.execute(SQL, [pk_value,])
                try:
                    db_vals = cur.fetchall()[0]
                    record = dict()
                    for col, val in zip(db_cols, db_vals):
                        record[col] = val
                    logging.debug('Retrieve successful')    
                    return rec_cls(**record, new=False)
                except IndexError:
                    raise errors.RecordNotFoundError('No {0}.{1} record matching {2} was found'.format(db_table, db_pk, pk_value))
                except Exception:
                    raise

    def create_record(self, vbr_object: record.VBRRecord) -> str:
        """Insert a VBR Record into the database
        """
        # NOTE: vbr_object is instance of a class defined in tableclasses

        # Get SQL attributes and data from VBR Record
        db_table = vbr_object.table_name
        db_pk = vbr_object.primary_key
        db_cols = vbr_object.field_names()
        db_values = vbr_object.field_values()

        logging.debug('Writing to table {0}'.format(db_table))

        # Extend with private session ID
        db_cols = list(db_cols)
        db_cols.append(constants.SESSION_FIELD)
        db_values = list(db_values)
        db_values.append(self.session)

        # enumerate column names
        sql_columns = ','.join(db_cols)

        # create a '%s' string for every data element
        sql_vars = ','.join(['%s' for d in db_cols])

        # Construct SQL statement including return of primary key
        # https://stackoverflow.com/a/5247723
        SQL = "INSERT INTO {} ({}) _VALUES ({}) RETURNING {};".format(
            db_table, sql_columns, sql_vars, db_pk)

        conn = self.db
        id_of_new_row = None
        # Using a pair of contexts will automatically roll back the pending transaction 
        # if an Exception is encountered
        with conn:
            with conn.cursor() as cur:
                logging.debug(cur.mogrify(SQL, db_values))
                cur.execute(SQL, db_values)
                # Get last row created
                # https://stackoverflow.com/a/5247723
                id_of_new_row = cur.fetchone()[0]
                conn.commit()
                logging.debug('Create successful: {0}.{1} = {2}'.format(db_table, db_pk, id_of_new_row))
                return str(id_of_new_row)

        # TODO - implement better failure handling

    def update_record(self, vbr_object: record.VBRRecord) -> NoReturn:
        """Update a VBR Record in the database
        """
        db_table = vbr_object.table_name
        db_pk = vbr_object.primary_key
        pk_value = vbr_object._VALUES.get(db_pk)
        db_cols = vbr_object.field_names(include_pk=False)
        db_values = vbr_object.field_values(include_pk=False)
        if pk_value is None:
            raise errors.ValidationError('Field {0} cannot be empty'.format(db_pk))
        
        # Create SQL statement
        data = []
        sets = []
        for col, val in zip(db_cols, db_values):
            sets.append('{0} = %s'.format(col))
            data.append(val)
        sets_sql = ','.join(sets)
        SQL = "UPDATE {0} SET {1} WHERE {2} = %s;".format(db_table, sets_sql, db_pk)
        # Add primary key value to end of data to support the WHERE clause above
        data.append(pk_value)
        conn = self.db
        with conn:
            with conn.cursor() as cur:
                logging.debug(cur.mogrify(SQL, data))
                cur.execute(SQL, data)
                conn.commit()
                logging.debug('Update successful')

    def delete_record(self, vbr_object: record.VBRRecord) -> NoReturn:
        """Delete a VBR Record from the database
        """
        # Get SQL attributes and data from VBR Record
        db_table = vbr_object.table_name
        db_pk = vbr_object.primary_key
        pk_value = vbr_object._VALUES.get(db_pk)
        SQL = "DELETE FROM {} WHERE {} = %s".format(
            db_table, db_pk)
        conn = self.db
        with conn:
            with conn.cursor() as cur:
                logging.debug(cur.mogrify(SQL, [pk_value,]))
                cur.execute(SQL, [pk_value,])
                conn.commit()
                logging.debug('Delete successful')
