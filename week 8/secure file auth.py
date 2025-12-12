import logging
import hashlib
from datetime import datetime
from getpass import getpass

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class User:
    def __init__(self, username, password, privilege, attempts=0, status="active"):
        self.username = username
        self._hash_password = self._hash(password)
        self.privilege_level = privilege
        self.login_attempts = attempts
        self.account_status = status

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def lock_account(self):
        self.account_status = "locked"

    def reset_login_attempts(self):
        self.login_attempts = 0

    def log_activity(self, message):
        with open("tracking_file.txt", "a") as f:
            f.write(f"{datetime.now()} - {self.username} - {message}\n")

    def authenticate(self, username_input, password_input):
        if username_input != self.username:
            print("Username not found.")
            return False

        if self.account_status != "active":
            logging.warning(f"Account {self.username} not active.")
            self.log_activity("attempted login but account inactive")
            return None

        if self._hash(password_input) == self._hash_password:
            self.reset_login_attempts()
            logging.info(f"User {self.username} authenticated successfully.")
            self.log_activity("logged in successfully")
            return True
        else:
            self.login_attempts += 1
            logging.warning(f"Failed login attempt {self.login_attempts} for {self.username}")
            self.log_activity(f"failed login attempt {self.login_attempts}")

            if self.login_attempts >= 3:
                self.lock_account()
                logging.error(f"Account {self.username} is now locked")
                self.log_activity("account locked due to failed attempts")

            return False

    def file(self):
        with open("file_log.txt", "a") as f:
            f.write(
                f"{datetime.now()} - USER: {self.username} | "
                f"PRIV: {self.privilege_level} | "
                f"ATTEMPTS: {self.login_attempts} | "
                f"STATUS: {self.account_status}\n"
            )

if __name__ == "__main__":
    user1 = User(username="yehia", password="mypassword", privilege="admin")

    while True:
        username_input = input("Please enter your username: ")
        password_input = getpass("Please enter your password: ")
        result = user1.authenticate(username_input, password_input)

        if result is True:
            print("Login successful!")
            user1.file()
            break
        elif result is False:
            print(f"Login failed! Attempt {user1.login_attempts}")
            if user1.account_status == "locked":
                print("Your account is now locked.")
                user1.file()
                break
        else:
            print("Account not active.")
            user1.file()
            break
