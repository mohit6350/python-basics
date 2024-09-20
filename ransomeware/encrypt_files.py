import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import secrets

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

# Function to encrypt a file
def encrypt_file(key, file_path):
    backend = default_backend()
    iv = secrets.token_bytes(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        file_data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Store the IV and encrypted data together
    encrypted_file_path = f"{file_path}.enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"Encrypted {file_path} -> {encrypted_file_path}")
    # Delete the original file after encryption
    os.remove(file_path)
    print(f"Deleted original file: {file_path}")

# Function to encrypt all files in a directory
def encrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)

if __name__ == "__main__":
    directory = "C:\\Users\\Khare\\Desktop\\test"
    password = "mohit123"
    salt = secrets.token_bytes(16)  # Random salt for key derivation
    key = derive_key(password, salt)

    # Save the salt to a file (required for decryption)
    with open('salt.bin', 'wb') as salt_file:
        salt_file.write(salt)

    encrypt_directory(directory, key)
