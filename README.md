# 🔐 Secure Password Manager

A cybersecurity-focused desktop application built using Python that securely stores and manages user credentials using strong encryption techniques.

This project demonstrates real-world security concepts including encryption, authentication, and secure data handling, packaged inside a simple and user-friendly GUI.

---

## 🚀 Features

* 🔑 Master password authentication
* 🔐 AES-based encryption using Fernet
* 🛡 Secure storage of credentials
* 🎲 Strong password generator
* 🖥 GUI application using Tkinter
* 📂 Local encrypted vault (JSON-based)
* 🔁 Persistent encryption key management

---

## 🧠 How It Works

* A **master password** is created and stored as a secure hash
* An **encryption key** is generated and saved locally
* All passwords are encrypted before storage
* Stored credentials are decrypted only when accessed
* The GUI allows easy interaction with the vault

---

## 🛠 Tech Stack

* Python 3
* Tkinter (GUI)
* Cryptography (Fernet encryption)
* JSON (data storage)
* Hashlib (password hashing)

---

## 📂 Project Structure

```
secure-password-manager/
│
├── gui_app.py              # GUI application
├── main.py                 # CLI version
├── crypto_utils.py         # Encryption utilities
├── password_manager.py     # Password storage logic
├── password_generator.py   # Password generator
├── auth.py                 # Master password authentication
├── vault.json              # Encrypted password storage
├── key.key                 # Encryption key
└── master.hash             # Hashed master password
```

---

## ▶️ Installation & Usage

### 1. Clone the repository

```
git clone https://github.com/yourusername/secure-password-manager.git
cd secure-password-manager
```

### 2. Install dependencies

```
pip install cryptography
```

### 3. Run the application

#### GUI version:

```
python gui_app.py
```

#### CLI version:

```
python main.py
```

---

## 🔐 Security Concepts Demonstrated

* Symmetric encryption (Fernet / AES)
* Password hashing (SHA-256)
* Secure credential storage
* Authentication mechanisms
* Basic key management

---

## ⚠️ Disclaimer

This project is developed for **educational purposes only** and is not intended to replace production-grade password managers.

---

## 🚀 Future Improvements

* Clipboard copy feature
* Password strength checker
* Search functionality
* Auto-lock vault
* SQLite encrypted database
* Dark mode UI
* Cloud sync (secure)

---

## 👨‍💻 Author

**Shubham Kumar Jha**
Aspiring Cybersecurity & Software Developer



---

## ⭐ Support

If you found this project helpful, consider giving it a **star ⭐** on GitHub.
