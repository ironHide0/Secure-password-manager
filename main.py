from crypto_utils import load_or_create_key
from password_manager import save_password, view_passwords
from password_generator import generate_password
from auth import verify_master_password

if not verify_master_password():
    print("Incorrect master password.")
    exit()

key = load_or_create_key()

while True:

    print("\nSecure Password Manager")
    print("1 Save password")
    print("2 View passwords")
    print("3 Generate password")
    print("4 Exit")

    choice = input("Select option: ")

    if choice == "1":
        site = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        save_password(site, username, password, key)

        print("Password stored securely.")

    elif choice == "2":
        view_passwords(key)

    elif choice == "3":
        length = int(input("Password length: "))
        print("Generated password:", generate_password(length))

    elif choice == "4":
        break
