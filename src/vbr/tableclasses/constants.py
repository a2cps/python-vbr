from ..pgrest import Column, Serial, String, LocalId


class Constants:
    PROJECT_NAMESPACE = 'tag:a2cps.org","'
    SERIAL_PRIMARY_KEY_COLUMN = Column(Serial, primary_key=True)
    STRING_NAMESPACE_COLUMN = Column(String, default=PROJECT_NAMESPACE)
    STRING_LOCALID_COLUMN = Column(LocalId)
    STRING_PERSISTENT_ID = Column(String, nullable=True)
