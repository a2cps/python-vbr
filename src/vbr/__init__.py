"""Virtual Biospecimen Repository Python API
"""
from . import api, pgrest, tableclasses, utils
import importlib.metadata

__version__ = importlib.metadata.version('python-vbr')

# from .client import VBR
