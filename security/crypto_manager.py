import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CryptoManager:
    """Handles master password derivation and AES encryption/decryption

    for exchange API keys and sensitive credentials.
    """

    def __init__(self, master_password: str, salt: bytes = None):
        if salt is None:
            # Generate a new salt if not provided (stored locally per installation)
            self.salt = os.urandom(16)
        else:
            self.salt = salt

        self._key = self._derive_key(master_password, self.salt)
        self._cipher = Fernet(self._key)

    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derives a 32-byte key from the master password using PBKDF2HMAC."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))

    def encrypt(self, plain_text: str) -> str:
        """Encrypts plain text string into Fernet token string."""
        return self._cipher.encrypt(plain_text.encode("utf-8")).decode("utf-8")

    def decrypt(self, cipher_text: str) -> str:
        """Decrypts Fernet token string back into plain text string."""
        return self._cipher.decrypt(cipher_text.encode("utf-8")).decode("utf-8")

    def get_salt_hex(self) -> str:
        """Returns salt formatted as hex string for storage."""
        return self.salt.hex()

    @staticmethod
    def salt_from_hex(hex_str: str) -> bytes:
        """Converts hex string back to salt bytes."""
        return bytes.fromhex(hex_str)
