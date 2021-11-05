"""Test features of SysEvent class.
"""
import pytest
import vbr


def test_default_status_on_init():
    """Event status should be RECEIVED when created."""
    event = vbr.tableclasses.VbrSysEventTable()
    assert event.get_status() == "RECEIVED"


def test_set_get_status():
    """Event status should be settable and gettable."""
    event = vbr.tableclasses.VbrSysEventTable()
    event.set_status("PROCESSING")
    assert event.get_status() == "PROCESSING"


def test_set_status_validate():
    """Should not be possible to set status to invalid value."""
    event = vbr.tableclasses.VbrSysEventTable()
    with pytest.raises(ValueError):
        event.set_status("0xDEADBEEF")
