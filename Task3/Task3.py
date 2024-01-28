import getpass
import codecs
import os

# Defining the const filename for the password file
PASSWORD_FILE = 'passwd.txt'

def encrypt(text):
    # ROT13 encryption
    return codecs.encode(text, 'rot_13')

def add_user():
    # Add a new user to the password file
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")
    password = encrypt(password)

    with open(PASSWORD_FILE, 'a') as f:
        f.write(f"{username}:{real_name}:{password}\n")
    print("User Created.")

def delete_user():
    # Delete a user from the password file
    username = input("Enter username: ")

    deleted = False  # Flag to track if user is deleted

    with open(PASSWORD_FILE, 'r') as f:
        lines = f.readlines()

    with open(PASSWORD_FILE, 'w') as f:
        for line in lines:
            if not line.startswith(f"{username}:"):
                f.write(line)
            else:
                deleted = True  # User found and deleted

    if deleted:
        print("User Deleted.")
    else:
        print("User not found.")

def change_password():
    # Change user password
    username = input("User: ")
    current_password = encrypt(getpass.getpass("Current Password: "))
    new_password = encrypt(getpass.getpass("New Password: "))
    confirm_password = encrypt(getpass.getpass("Confirm: "))

    if new_password == confirm_password:
        with open(PASSWORD_FILE, 'r') as f:
            lines = f.readlines()

        with open(PASSWORD_FILE, 'w') as f:
            for line in lines:
                if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                    f.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
                else:
                    f.write(line)

        print("Password changed.")
    else:
        print("Passwords do not match. Nothing changed.")

def login():
    # User login
    username = input("User: ")
    password = encrypt(getpass.getpass("Password: "))

    with open(PASSWORD_FILE, 'r') as f:
        for line in f:
            user_info = line.strip().split(':')
            if user_info[0] == username and user_info[2] == password:
                print("Access granted.")
                return

    print("Access denied.")

def main():
    # Check if the password file exists
    if not os.path.exists(PASSWORD_FILE):
        print("Password file not found.")
        return

    while True:
        command = input("Enter command (adduser, deluser, passwd, login, quit): ")

        if command == "adduser":
            add_user()
        elif command == "deluser":
            delete_user()
        elif command == "passwd":
            change_password()
        elif command == "login":
            login()
        elif command == "quit":
            break
        else:
            print("Invalid command. Please use adduser, deluser, passwd, login, or quit.")

main()
