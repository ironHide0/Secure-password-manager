import tkinter as tk
from tkinter import messagebox

from crypto_utils import load_or_create_key
from password_manager import save_password, view_passwords
from password_generator import generate_password
from auth import verify_master_password


# verify master password
if not verify_master_password():
    print("Access denied")
    exit()

key = load_or_create_key()


# main window
window = tk.Tk()
window.title("Secure Password Manager")
window.geometry("400x300")


# labels
tk.Label(window, text="Website").pack()
site_entry = tk.Entry(window)
site_entry.pack()

tk.Label(window, text="Username").pack()
user_entry = tk.Entry(window)
user_entry.pack()

tk.Label(window, text="Password").pack()
pass_entry = tk.Entry(window)
pass_entry.pack()


# functions
def save():
    site = site_entry.get()
    user = user_entry.get()
    password = pass_entry.get()

    save_password(site, user, password, key)

    messagebox.showinfo("Success", "Password saved securely")


def generate():
    password = generate_password(12)
    pass_entry.delete(0, tk.END)
    pass_entry.insert(0, password)


def view():
    view_passwords(key)


# buttons
tk.Button(window, text="Save Password", command=save).pack(pady=5)
tk.Button(window, text="Generate Password", command=generate).pack(pady=5)
tk.Button(window, text="View Passwords", command=view).pack(pady=5)


window.mainloop()