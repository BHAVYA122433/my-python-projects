from cryptography.fernet import Fernet
import os

# Generate and save a key for encryption (only if it doesn't already exist)
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved to key.key.")
    else:
        print("Encryption key already exists.")

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to add a new password
def add_password(service, username, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password.decode()}\n")
    print(f"Password for {service} added.")

# Function to view all stored passwords
def view_passwords(key):
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            for line in file:
                service, username, encrypted_password = line.strip().split(",")
                decrypted_password = decrypt_password(encrypted_password.encode(), key)
                print(f"Service: {service}, Username: {username}, Password: {decrypted_password}")
    else:
        print("No passwords stored yet.")

# Function to delete a password
def delete_password(service):
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
        
        with open("passwords.txt", "w") as file:
            for line in lines:
                if line.strip().split(",")[0] != service:
                    file.write(line)
        print(f"Password for {service} deleted.")
    else:
        print("No passwords stored yet.")

def main():
    # Ensure the encryption key is generated only once
    generate_key()
    key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(service, username, password, key)
        elif choice == "2":
            view_passwords(key)
        elif choice == "3":
            service = input("Enter service name to delete: ")
            delete_password(service)
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
