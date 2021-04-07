from person.staff import Staff
from local_db.create_table import conn


class StaffMember(Staff):
    def __init__(self, first_name, last_name, tax_number, username, password):
        super().__init__(first_name, last_name, tax_number, username, password)

    def get_staff_info(self):
        # Get Staff information
        correct_info = False
        while not correct_info:
            self.first_name = input("Input staff first name:    ")
            self.last_name = input("Input staff last name:    ")
            self.tax_number = input(int("Input staff tax number:     "))
            print("Name:", self.first_name, self.last_name, "    tax.no:", self.tax_number)
            check = input("Is the above information correct? Y/N".upper())
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

    def create_username(self):
        correct_info = False
        while not correct_info:
            self.username = input("Choose a username:    ")
            print("Username:", self.username)
            check = input("Is the above information correct? Y/N".upper())
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

    def create_password(self):
        # Get Staff password
        correct_info = False
        while not correct_info:
            self.password = input("Choose a password:    ")
            password_check = input("Please retype your password:    ")
            if self.password == password_check:
                correct_info = True
            else:
                print("Please type the same password.")

    def register_staff(self, first_name, last_name, tax_number, username, password):
        conn.execute(f"INSERT INTO Staff"
                     f"(FirstName, LastName, TaxNumber, Username, Password)"
                     f"VALUES"
                     f"({self.first_name}, {self.last_name}, {self.tax_number}, {self.username}, {self.password});")
        # Save the changes.
        self.conn.commit()
