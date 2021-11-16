"""Test REDcap event id/name mappings.
"""
import pytest
import vbr


def test_redcap_event_to_vbr_protocol():
    assert (
        vbr.utils.redcaptasks.redcap_event_to_vbr_protocol("informed_consent_arm_1")
        == 2
    )


def test_redcap_event_to_vbr_protocol_valuerror():
    with pytest.raises(ValueError):
        vbr.utils.redcaptasks.redcap_event_to_vbr_protocol("deadbeef")


def test_redcap_event_id_to_unique_event_name():
    assert (
        vbr.utils.redcaptasks.redcap_event_id_to_unique_event_name(41)
        == "informed_consent_arm_1"
    )


def test_redcap_event_id_to_unique_event_name_valuerror():
    with pytest.raises(ValueError):
        vbr.utils.redcaptasks.redcap_event_id_to_unique_event_name(-1)


@pytest.mark.parametrize("test_input,expected", [("14", "2"), ("29", "3"), ("25", "1")])
def test_redcap_project_id_to_vbr_project(test_input, expected):
    assert vbr.utils.redcaptasks.redcap_to_vbr_project_id(test_input) == expected
