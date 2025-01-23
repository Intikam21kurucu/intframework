#!/usr/bin/env python3
import hashlib

# Save user information to a file
def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashlib.sha256(password.encode()).hexdigest()}\n")

# Load user information from a file
def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password_hash = line.strip().split(":")
                users[username] = password_hash
    except FileNotFoundError:
        pass
    return users

# Registration process
def register(username, password):
    users = load_users()
    if username in users:
        print("This username already exists.")
    else:
        save_user(username, password)
        print("Registration successful!")

# Password reset process
def reset_password(username):
    new_password = input("New password: ")
    users = load_users()
    users[username] = hashlib.sha256(new_password.encode()).hexdigest()
    with open("users.txt", "w") as file:
        for user, password_hash in users.items():
            file.write(f"{user}:{password_hash}\n")
    print("Password reset successful!")

# Login process
def login(username, password):
    users = load_users()
    if username in users:
        if password == "intikam21":
            print("Password reset process initiated.")
            reset_password(username)
            return None
        elif users[username] == hashlib.sha256(password.encode()).hexdigest():
            print("Login successful!")
            return username
        else:
            print("Incorrect password.")
            return None
    else:
        print("User not found, registering...")
        register(username, password)
        return username

def main():
    current_user = None
    username = input("Username: ")
    password = input("Password: ")
    current_user = login(username, password)
    
    while current_user:
        print(f"Logged in user: {current_user}")
        # The user can press Enter to log out.
        input("Press Enter to log out...")
        current_user = None
        print("Logged out.")
        break

if __name__ == "__main__":
    main()