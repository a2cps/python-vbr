from ...pgrest import Column, LocalId, Serial, String


class REDCapConstants:
    GUID = Column(
        String,
        nullable=True,
        comments="REDCap GUID used as the persistent id for the subject",
    )
    RECORD_ID = Column(String, comments="REDCap record_id identifying subject")
