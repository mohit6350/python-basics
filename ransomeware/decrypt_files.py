import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

# Function to derive a key from a password
def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to decrypt a file
def decrypt_file(key, file_path):
    backend = default_backend()

    with open(file_path, 'rb') as f:
        iv = f.read(16)  # The first 16 bytes are the IV
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    decrypted_file_path = file_path.replace('.enc', '')

    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"Decrypted {file_path} -> {decrypted_file_path}")
    os.remove(file_path)
    print(f"Deleted original file: {file_path}")

# Function to decrypt all files in a directory
def decrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".enc"):
                file_path = os.path.join(root, file)
                decrypt_file(key, file_path)

if __name__ == "__main__":
    directory = "C:\\Users\\Khare\\Desktop\\test"
    password = "mohit123"

    # Load the salt used during encryption
    with open('salt.bin', 'rb') as salt_file:
        salt = salt_file.read()

    key = derive_key(password, salt)
    decrypt_directory(directory, key)
