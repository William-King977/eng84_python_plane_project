from prettytable import PrettyTable
from local_db import db_runner


class BookingManager:

    def __init__(self):
        self.conn = db_runner.DBRunner()

    def get_passenger_info(self):
        # Get Passenger information
        correct_info = False
        while not correct_info:
            self.first_name = input("Input passenger's first name: ")
            self.last_name = input("Input passenger's last name: ")
            self.passport_number = input("Input the passenger's passport number: ")
            self.ticket_number = input("Input passenger's ticket number: ")
            print("Name:", self.first_name, "| Last Name:", self.last_name, "| Ticket.no:", self.ticket_number,
                  "| Passport.no:", self.passport_number)
            check = input("Is the above information correct (Y/N)? ").upper()
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True
        self.__register_passenger()

    def __register_passenger(self):
        # Add the passenger and update the number of passengers for that flight.
        self.conn.register_passenger(self.first_name, self.last_name, self.ticket_number,
                                     self.passport_number)
        print("Passenger registered successfully.")

    def passenger_booking(self):
        # Ask for details.
        while True:
            passenger_id = int(input("Input the passenger ID: "))
            flight_id = int(input("Input the flight ID: "))
            print(f"Passenger ID: {passenger_id} | Flight ID: {flight_id}")
            check = input("Is the above information correct (Y/N)? ").upper()
            if check in ["YES", "TRUE", "T", "Y"]:
                break

        # If the flight is full.
        if self.conn.is_flight_full(flight_id):
            print("Sorry, the flight is full.")
        # Check if the passenger is already on the selected flight.
        elif self.conn.is_passenger_on_flight(passenger_id, flight_id):
            print("Sorry, the passenger is already assigned to this flight.")
        else:
            self.conn.create_booking(passenger_id, flight_id)
            self.conn.update_number_of_flight_passengers(flight_id)
            print("Passenger added to the flight successfully.")

    def display_all_passengers(self):
        all_passengers = self.conn.get_all_passengers()
        passenger_table = PrettyTable(["Passenger ID", "First Name", "Last Name",
                                       "Ticket Number", "Passport Number"])
        for passenger in all_passengers:
            passenger_table.add_row(passenger)
        print(passenger_table)
        input("Press enter to continue.")


if __name__ == "__main__":
    BookingManager()


