"""Test ability to generate table definitions.
"""
from vbr import tableclasses


def test_table_definitions():
    tdefs = tableclasses.table_definitions()
    assert len(tdefs) > 0
