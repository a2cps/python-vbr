"""Test features of Table class using a mock class definition.
"""
import pytest
import vbr


class ExampleTable(vbr.pgrest.Table):
    """Comment"""

    identifier = vbr.pgrest.Column(vbr.pgrest.Serial)
    text_field = vbr.pgrest.Column(vbr.pgrest.String, comments="Comment")
    text_field_nullable = vbr.pgrest.Column(vbr.pgrest.String, nullable=True)
    bool_field = vbr.pgrest.Column(vbr.pgrest.Boolean)


def test_instance_properties():
    """Class instance have properties with values provided at __init__()"""
    table = ExampleTable(identifier=1, text_field="Text", bool_field=True)
    assert table.identifier == 1
    assert table.text_field == "Text"
    assert table.text_field_nullable == None
    assert table.bool_field == True
    # Nullable field should not be in the dict representation of class instance
    assert "text_field_nullable" not in table.dict().keys()
    # Non-nullable field should
    assert "text_field" in table.dict().keys()


def test_url_and_name():
    """Root URL and name are snake_cased class name"""
    table = ExampleTable()
    assert table.__schema__.root_url == "example_table"
    assert table.__schema__.table_name == "example_table"


def test_comments():
    """Table comment inherits from class docstring"""
    table = ExampleTable()
    assert table.__schema__.comment == "Comment"


def test_column_comments():
    """Column comment available via __schema__"""
    table = ExampleTable()
    assert table.__schema__.columns["text_field"]["comments"] == "Comment"


def test_primary_key():
    """Table primary key value is available via function"""
    table = ExampleTable()
    assert table.primary_key_id() is None
    # User should never do this but this is how _pkid is populated at init() time
    table = ExampleTable(_pkid=1)
    assert table.primary_key_id() == 1
