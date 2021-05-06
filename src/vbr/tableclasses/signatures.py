"""Blake2B keyed signature and validation
"""
import hashlib

SIGNATURE_KEY = b'?Vh%5),2)_+UtjpZ.#MV%M}ENE[n;X]d'
SIGNATURE_LENGTH = 16
SIGNATURE_PERSONALIZATION = b'python-vbr'

__all__ = ['sign', 'validate']


def sign(elements,
         key=SIGNATURE_KEY,
         digest_length=SIGNATURE_LENGTH,
         personalization=SIGNATURE_PERSONALIZATION) -> bytes:
    """Return a cryptographically-distinct signature for a list of data elements
    """
    if not isinstance(elements, list):
        elements = [elements]
    sig_els = []
    for el in elements:
        sig_els.append(str(el))
    sig_text = '|'.join(sig_els)
    sig_text = sig_text.encode('utf-8')
    return hashlib.blake2b(sig_text,
                           digest_size=digest_length,
                           person=personalization,
                           key=key).hexdigest()


def validate(elements,
             signature,
             key=SIGNATURE_KEY,
             digest_length=SIGNATURE_LENGTH,
             personalization=SIGNATURE_PERSONALIZATION) -> bool:
    """Validate a signature for a list of data elements
    """
    sig = sign(elements,
               key=key,
               digest_length=digest_length,
               personalization=personalization)
    return sig == signature
