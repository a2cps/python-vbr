import hashlib
from . import record

SIGNATURE_FIELD = '_signature'

class VBRUniqueRecord(record.VBRRecord):
    SIGNATURE_FIELDS = []
    SIGNATURE_FIELD_NAME = SIGNATURE_FIELD
    SIGNATURE_SALT = 'mWKGVzNJcZ*/nn5s^>dC+#j8'
    SIGNATURE_LENGTH = 24

    @property
    def unique_field(self) -> str:
        return self.UNIQUE_FIELD

    @property
    def signature(self) -> str:
        if len(self.SIGNATURE_FIELDS) > 0:
            sig_fields = self.SIGNATURE_FIELDS
        else:
            sig_fields = self.field_names()
        sig_els = [self.SIGNATURE_SALT]
        for sf in sig_fields:
            sig_els.append(str(self._VALUES.get(sf)))
        sig_txt = '|'.join(sig_els)
        sig_hex = hashlib.sha256(sig_txt.encode('utf-8')).hexdigest()[:self.SIGNATURE_LENGTH-1]
        return sig_hex

    @classmethod
    def field_names(cls, include_pk:bool=False) -> tuple:
        fn = list(super().field_names(include_pk))
        fn.append(cls.SIGNATURE_FIELD_NAME)
        return tuple(fn)
    
    def field_values(self, include_pk:bool=False) -> tuple:
        fv = list(super().field_values(include_pk))
        fv.append(self.signature)
        return tuple(fv)

