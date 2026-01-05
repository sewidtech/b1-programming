import logging
import hashlib
from datetime import datetime
from getpass import getpass


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

VALID_PRIVILEGES = {"admin", "owner", "member"}

class User:
    def __init__(self, username, password, privilege):
        if privilege not in VALID_PRIVILEGES:
            raise ValueError("Invalid privilege level")

        self.username = username
        self.__password_hash = self.__hash(password)
        self.__privilege_level = privilege
        self.__login_attempts = 0
        self.__account_status = "active"

    def __hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def get_privilege(self):
        return self.__privilege_level

    def get_status(self):
        return self.__account_status

    def get_attempts(self):
        return self.__login_attempts

    def __lock_account(self):
        self.__account_status = "locked"

    def __reset_attempts(self):
        self.__login_attempts = 0

    def __log_activity(self, message):
        with open("tracking_file.txt", "a") as f:
            f.write(f"{datetime.now()} - {self.username} - {message}\n")

    def authenticate(self, username_input, password_input):
        if self.__account_status != "active":
            logging.warning("Account inactive")
            self.__log_activity("login blocked (inactive)")
            return False

        if username_input != self.username:
            logging.warning("Invalid username")
            return False

        if self.__hash(password_input) == self.__password_hash:
            self.__reset_attempts()
            logging.info("Authentication successful")
            self.__log_activity("login successful")
            return True

        self.__login_attempts += 1
        logging.warning(f"Failed login attempt {self.__login_attempts}")
        self.__log_activity(f"failed login attempt {self.__login_attempts}")

        if self.__login_attempts >= 3:
            self.__lock_account()
            logging.error("Account locked")
            self.__log_activity("account locked")

        return False


if __name__ == "__main__":
    users = [
        User("yehia", "mypassword", "admin"),
        User("mike", "password123", "member")
    ]
    print("Welcome to system.\n")
    username_input = input("Username: ")
    password_input = getpass("Password: ")

    user = next((u for u in users if u.username == username_input), None)

    if user and user.authenticate(username_input, password_input):
        print("Login successful")
        print(f"Privilege level: {user.get_privilege()}")
    else:
        print("Login failed")
