from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()
