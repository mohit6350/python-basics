import pyAesCrypt
import os

def encrypt_file(file_path, password):
    buffer_size = 64 * 1024  # 64 KB
    temp_file_path = file_path + ".enc"
    
    # Encrypt the file and write to a temporary file
    pyAesCrypt.encryptFile(file_path, temp_file_path, password, buffer_size)
    
    # Replace the original file with the encrypted file
    os.replace(temp_file_path, file_path)
    print("File encrypted successfully.")

def decrypt_file(file_path, password):
    buffer_size = 64 * 1024  # 64 KB
    temp_file_path = file_path + ".dec"
    
    # Decrypt the file and write to a temporary file
    pyAesCrypt.decryptFile(file_path, temp_file_path, password, buffer_size)
    
    # Replace the original file with the decrypted file
    os.replace(temp_file_path, file_path)
    print("File decrypted successfully.")

# Example usage
file_path = 'C://Users//Khare//Desktop//nf//1.png'
password = "password123"  # Your chosen password

# Encrypt the file
#encrypt_file(file_path, password)

# Decrypt the file
decrypt_file(file_path, password)
