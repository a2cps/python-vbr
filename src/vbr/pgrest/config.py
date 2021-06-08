"""Configuration for PgREST classes
"""

__all__ = ['Config']


class Config(object):
    """Configuration class mostly used for feature gating to match the current PgREST schema
    """
    COLUMN_COMMENTS = False
    COLUMN_USE_FOREIGN_KEY_PROPERTY_NAME = False
    TABLE_CONSTRAINTS = False
    TABLE_COMMENTS = False
