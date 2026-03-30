import json
from crypto_utils import encrypt_password, decrypt_password

def save_password(site, username, password, key):
    encrypted = encrypt_password(key, password)

    data = {
        "site": site,
        "username": username,
        "password": encrypted
    }

    try:
        with open("vault.json", "r") as file:
            vault = json.load(file)
    except:
        vault = []

    vault.append(data)

    with open("vault.json", "w") as file:
        json.dump(vault, file, indent=4)

def view_passwords(key):
    try:
        with open("vault.json", "r") as file:
            vault = json.load(file)
    except:
        print("No passwords stored yet.")
        return

    for entry in vault:
        decrypted = decrypt_password(key, entry["password"])
        print("\nSite:", entry["site"])
        print("Username:", entry["username"])
        print("Password:", decrypted)
