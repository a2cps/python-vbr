"""Test imports of package and select submodules.
"""


def test_package_import():
    try:
        import vbr
    except ImportError:
        raise


def test_pgrest_submodule_imports():
    try:
        from vbr import pgrest
    except ImportError:
        raise


def test_client_submodule_imports():
    try:
        from vbr.client import VBR
    except ImportError:
        raise


def test_api_submodule_imports():
    try:
        from vbr.api import get_vbr_api_client, VBR_Api
    except ImportError:
        raise
