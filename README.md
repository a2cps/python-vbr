# Virtual Biospecimen Repository (VBR) Python Library

This is a package for working with the TACC Virtual Biospecimen Repository database. Details on configuring and setting up an instance of VBR is not covered by this documentation. 

## Installation

```shell
git clone https://github.com/A2CPS/python-vbr
cd python-vbr
pip install --user .
```

## Usage

### Connect to VBR Database

```shell
>>> import vbr
>>> d = vbr.VBR(config={'ip': 'localhost', 'user': 'vbruser', 'pass': 'vbrpass', 'db': 'a2cps})
DEBUG:root:VBR Session: b00251b3773344bf8a00b229ec1da5b9
>>> d.session
b00251b3773344bf8a00b229ec1da5b9
```

**NOTE** Sessions are intended for supporting development use cases only. 

It is also possible to configure a VBR connection using the environment variables `VBR_HOST`, `VBR_DATABASE`, `VBR_USERNAME`, and `VBR_PASSWORD`. Values passed in via the `config` dictionary override environment variables. 
```shell
% export VBR_PASSWORD='s3cr379@$$w0rD'
% python
>>> import vbr
d = vbr.VBR(config={'ip': 'localhost', 'user': 'vbruser', 'db': 'a2cps'})
DEBUG:root:VBR Session: b00251b3773344bf8a00b229ec1da5b9
# The database connection will be configured with password from the environment and the specified dict
```

### Direct Database Operations

The `db` property of a `VBR` class instance is a standard `psycopg2` connection. It supports all documented `psycopg2` functions. The `VBR` class is augmented with several helper functions. 

```shell
>>> cur = d.db.cursor()
# Select first 10 biosamples
>>> cur.execute("SELECT * FROM dataset;")
>>> cur.fetchone()
```

### Table Classes

Each VBR table is represented by a table class. You can find a comprehensive list of these via `help(vbr.tableclasses)`. You can find signature for instantiating each table class via the `fields()` classmethod. 

```shell
# Get signature for creating a new DataEvent
>>> vbr.DataEvent.fields()
[('data_event_id', 'serial', True), ('protocol', 'integer', False), ('rank', 'integer', False), ('event_ts', 'timestamp', False), ('event_count', 'integer', False), ('subject', 'varchar', False), ('performed_by', 'integer', False), ('status', 'integer', False), ('reason', 'integer', False), ('dataset', 'integer', False)]
# Create an instance of a DataEvent
>>> de = vbr.DataEvent(data_event_id=None, status=1)
DEBUG:root:New VBRRecord: {'data_event_id': None, 'protocol': None, 'rank': None, 'event_ts': None, 'event_count': None, 'subject': None, 'performed_by': None, 'status': 1, 'reason': None, 'dataset': None}
# SQL field names for the DataEvent
>>> de.field_names()
('protocol', 'rank', 'event_ts', 'event_count', 'subject', 'performed_by', 'status', 'reason', 'dataset')
# SQL-compatible values for the DataEvent
>>> de.field_values()
(None, None, None, None, None, None, 1, None, None)
```

**Validation**

The VBRRecord parent class attempts to enforce basic validation at construction time.

```shell
# 1. You must supply all required arguments when constructing a VBR Record
>>> org = vbr.Organization(organization_id=None, name='Flavor Town')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taco/python-vbr/src/vbr/record.py", line 100, in __init__
    raise errors.ValidationError(
vbr.errors.ValidationError: url is required but was not provided
# 2. You cannot stuff arbitrary arguments into the VBR Record constructor
>>> de = vbr.DataEvent(data_event_id=None, status=1, foobar='abcdef')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taco/python-vbr/src/vbr/record.py", line 105, in __init__
    raise errors.ValidationError(
vbr.errors.ValidationError: Cannot process unknown kwargs: {'foobar': 'abcdef'}
```

### Retrieve a Record

```shell
# Specify the value for primary key and a table name
>>> tacc = d.retrieve_record(1, 'organization')
DEBUG:root:b'SELECT organization_id,url,name,description,synonyms FROM organization WHERE organization_id = 1 LIMIT 1'
DEBUG:root:Retrieve successful
DEBUG:root:VBRRecord: {'organization_id': 1, 'url': 'tacc.utexas.edu', 'name': 'TACC', 'description': 'Texas Advanced Computing Center', 'synonyms': 'DCC'}
# Get the value for a field
>>> tacc.get_field('url')
'tacc.utexas.edu'
# Not all tables are currently supported
>>> a2cps = d.retrieve_record(1, 'project')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taco/python-vbr/src/vbr/connection.py", line 63, in retrieve_record
    rec_cls = tableclasses.class_from_table(table_name)
  File "/home/taco/python-vbr/src/vbr/tableclasses.py", line 23, in class_from_table
    raise errors.TableNotSupported('{0} is not currently supported by the VBR module'.format(table_name))
vbr.errors.TableNotSupported: project is not currently supported by the VBR module
```


### Create a Record

```shell
# Create a new DataEvent
>>> de = vbr.DataEvent(data_event_id=None, status=1)
DEBUG:root:New VBRRecord: {'data_event_id': None, 'protocol': None, 'rank': None, 'event_ts': None, 'event_count': None, 'subject': None, 'performed_by': None, 'status': 1, 'reason': None, 'dataset': None}
# Insert into the database
>>> d.create_record(de)
# Insertion returns the primary key of the created record
'1'
```

### Update a Record

```shell
# Retrieve a record from the organizations table
>>> a = d.retrieve_record(1, 'organization')
DEBUG:root:b'SELECT organization_id,url,name,description,synonyms FROM organization WHERE organization_id = 1 LIMIT 1'
DEBUG:root:Retrieve successful
DEBUG:root:New VBRRecord: {'organization_id': 1, 'url': 'tacc.utexas.edu', 'name': 'TACC', 'description': 'Texas Advanced Computing Center', 'synonyms': 'DCC'}
# Confirm that 'a' is an "Organization" type
>>> type(a)
<class 'vbr.tableclasses.Organization'>
# Update the value of 'synonyms' in the local Organization object
>>> a.set_field('synonyms', 'DCC CI')
'DCC CI'
# Update the database record with the contents of a
>>> d.update_record(a)
DEBUG:root:b"UPDATE organization SET url = 'tacc.utexas.edu',name = 'TACC',description = 'Texas Advanced Computing Center',synonyms = 'DCC CI' WHERE organization_id = 1;"
DEBUG:root:Update successful
# Retrieve the record to confirm the write was successful 
>>> a = d.retrieve_record(1, 'organization')
DEBUG:root:b'SELECT organization_id,url,name,description,synonyms FROM organization WHERE organization_id = 1 LIMIT 1'
DEBUG:root:Retrieve successful
DEBUG:root:New VBRRecord: {'organization_id': 1, 'url': 'tacc.utexas.edu', 'name': 'TACC', 'description': 'Texas Advanced Computing Center', 'synonyms': 'DCC CI'}
# Note that the organization has a new synonym 'CI'
```

### Delete a Record

```shell
# Create a Table Class instance with the primary key value
>>> de = vbr.DataEvent(data_event_id=277)
DEBUG:root:VBRRecord: {'data_event_id': 277, 'protocol': None, 'rank': None, 'event_ts': None, 'event_count': None, 'subject': None, 'performed_by': None, 'status': None, 'reason': None, 'dataset': None}
# Delete the record 
>>> d.delete_record(de)
DEBUG:root:b'DELETE FROM data_event WHERE data_event_id = 277'
DEBUG:root:Delete successful
# Attempt to retrieve deleted record fails with RecordNotFoundError error
>>> dd = d.retrieve_record(277, 'data_event')
DEBUG:root:b'SELECT data_event_id,protocol,rank,event_ts,event_count,subject,performed_by,status,reason,dataset FROM data_event WHERE data_event_id = 277 LIMIT 1'
Traceback (most recent call last):
  File "/home/taco/python-vbr/src/vbr/connection.py", line 80, in retrieve_record
    db_vals = cur.fetchall()[0]
IndexError: list index out of range
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taco/python-vbr/src/vbr/connection.py", line 87, in retrieve_record
    raise errors.RecordNotFoundError('No {0}.{1} record matching {2} was found'.format(db_table, db_pk, pk_value))
vbr.errors.RecordNotFoundError: No data_event.data_event_id record matching 277 was found
```

### Utility functions

## Contributing

_Coming soon_
