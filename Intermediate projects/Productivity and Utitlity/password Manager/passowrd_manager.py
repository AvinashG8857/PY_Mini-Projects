import json
import os
from cryptography.fernet import Fernet

# Generate or load encryption key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
cipher = Fernet(key)

# Load stored passwords
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            return json.load(f)
    return {}

# Save passwords
def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

# Add password
def add_password(account, username, password):
    passwords = load_passwords()
    encrypted_pw = cipher.encrypt(password.encode()).decode()
    passwords[account] = {"username": username, "password": encrypted_pw}
    save_passwords(passwords)
    print("Password added successfully!")

# Retrieve password
def get_password(account):
    passwords = load_passwords()
    if account in passwords:
        encrypted_pw = passwords[account]["password"]
        decrypted_pw = cipher.decrypt(encrypted_pw.encode()).decode()
        print(f"Account: {account}")
        print(f"Username: {passwords[account]['username']}")
        print(f"Password: {decrypted_pw}")
    else:
        print("Account not found.")

# Delete password
def delete_password(account):
    passwords = load_passwords()
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Account not found.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            account = input("Enter account name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(account, username, password)
        elif choice == "2":
            account = input("Enter account name: ")
            get_password(account)
        elif choice == "3":
            account = input("Enter account name: ")
            delete_password(account)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
