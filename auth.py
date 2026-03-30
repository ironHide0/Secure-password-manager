import hashlib
import os

MASTER_FILE = "master.hash"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password():
    password = input("Create master password: ")
    hashed = hash_password(password)

    with open(MASTER_FILE, "w") as f:
        f.write(hashed)

def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        setup_master_password()

    password = input("Enter master password: ")
    hashed = hash_password(password)

    with open(MASTER_FILE, "r") as f:
        stored_hash = f.read()

    return hashed == stored_hash
