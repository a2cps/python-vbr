class GenericRecordError(Exception):
    pass


class ValidationError(GenericRecordError):
    pass


class TableNotSupported(GenericRecordError):
    pass


class DuplicateSignature(GenericRecordError):
    pass


class GenericVBRError(Exception):
    pass


class ConnectionFailedError(GenericVBRError):
    pass


class RecordNotFoundError(GenericVBRError):
    pass


class NotUniqueError(GenericVBRError):
    pass
