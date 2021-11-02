from vbr.pgrest import Column, Serial, String, LocalId


class Constants:
    SERIAL_PRIMARY_KEY_COLUMN = Column(Serial, primary_key=True)
