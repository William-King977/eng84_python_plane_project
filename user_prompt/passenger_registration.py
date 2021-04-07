import sqlite3
from person.passenger import Passenger


class BookingManager(Passenger):
    conn = sqlite3.connect('PlaneProjectDB.db')
    cursor = conn.cursor()

    def __init__(self, first_name, last_name, tax_number, passport_number):

        super().__init__(first_name, last_name, tax_number, passport_number)

        self.start_connection()
        self.get_passenger_info()

    def start_connection(self):
        try:
            sqliteConnection = sqlite3.connect('PlaneProjectDB.db')
            cursor = sqliteConnection.cursor()
            print("Successfuly connected")
        except sqlite3.Error as error:
            print("Failed to connect", error)
        else:
            return "Connection Successful"

    def get_passenger_info(self):
        # Get Passenger information
        correct_info = False
        while not correct_info:
            self.first_name = input("Input passengers first name:    ")
            self.last_name = input("Input passengers last name:    ")
            self.passport_number = input("Input the passengers passport number:")
            self.tax_number = input("Input passengers tax number:     ")
            print("Name:", self.first_name, "Last Name", self.last_name, "tax.no:", self.tax_number, "and Passport.no:", self.passport_number)
            check = input("Is the above information correct? Y/N".upper())
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

        conn = sqlite3.connect('PlaneProjectDB.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Passengers(FirstName, LastName, PassportNumber, TaxNumber)
        VALUES (?,?,?,?)
        """, (self.first_name, self.last_name, self.passport_number, self.tax_number))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    BookingManager('','','','')


