# Virtual Biospecimen Repository (VBR) Python Library

This is a package for working with the TACC Virtual Biospecimen Repository database. 

## Installation

```shell
git clone https://github.com/A2CPS/python-vbr
cd python-vbr
pip install --user .
```

## Usage

### Connect to VBR Database

VBR is built atop the Tapis V3 pgrest service. The VBR constructor requires an 
active, valid Tapis API client to be passed in its constructor. 

```shell
>>> import vbr
>>> from tapipy.tapis import Tapis
>>> t = Tapis(base_url='https://a2cps.tapis.io', username='<username>', password='<password>')
>>> d = vbr.VBR(t)
>>> d.list_tables()
[{'table_id': 33, 'table_name': 'organization', 'root_url': 'organization', 'primary_key': 'organization_id'}]
```

It is also possible to configure a VBR connection using the environment variables `VBR_HOST`, `VBR_DATABASE`, `VBR_USERNAME`, and `VBR_PASSWORD`.

```shell
>>> import vbr
>>> t = vbr.client.connection.TapisUserEnv()
>>> d = vbr.VBR(t)
>>> d.list_tables()
[{'table_id': 33, 'table_name': 'organization', 'root_url': 'organization', 'primary_key': 'organization_id'}]
```

### Direct Operations

The `client` property of a `VBR` class instance is a standard `tapipy` connection. It supports all documented `tapipy` functions. API methods tailored to the VBR are described later. 

```shell
>>> resp = d.client.pgrest.get_in_collection(collection='organization', item='1')
```

### VBRRecord Table Classes

Each VBR table is represented by a table class. You can find a comprehensive list of these via `help(vbr.tableclasses)`. You can find signature for instantiating each table class via the `fields()` classmethod. 

*Examples coming soon*

**Validation**

The Table parent class implements basic validation at object construction time.

*Examples coming soon*


### Retrieve a Record

*Examples coming soon*


### Create a Record

*Examples coming soon*


### Update a Record

*Examples coming soon*

### Delete a Record

*Examples coming soon*

### Utility functions

*Coming soon*

## Contributing

*Coming soon*
