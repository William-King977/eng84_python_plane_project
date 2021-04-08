from local_db import db_runner


class RegisterStaff:

    def __init__(self):
        self.get_staff_info()
        self.create_username()
        self.create_password()
        self.register_new_staff()

    def get_staff_info(self):
        # Get Staff information
        correct_info = False
        while not correct_info:
            self.first_name = input("Input staff first name: ")
            self.last_name = input("Input staff last name: ")
            print("First name:", self.first_name, "| Last name:", self.last_name)
            check = input("Is the above information correct (Y/N)? ").upper()
            if check.upper() in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

    def create_username(self):
        correct_info = False
        while not correct_info:
            self.username = input("Choose a username: ")
            print("Username:", self.username)
            check = input("Is the above information correct (Y/N)? ").upper()
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

    def create_password(self):
        # Get Staff password
        correct_info = False
        while not correct_info:
            self.password = input("Choose a password: ")
            password_check = input("Please retype your password: ")
            if self.password == password_check:
                correct_info = True
            else:
                print("Please type the same password.")

    def register_new_staff(self):
        conn = db_runner.DBRunner()
        conn.register_staff(self.first_name, self.last_name, self.username, self.password)
        print("Registration successful.")


if __name__ == "__main__":
    RegisterStaff()
