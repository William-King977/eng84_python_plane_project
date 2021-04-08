from local_db import db_runner


class BookingManager:

    def __init__(self):
        self.conn = db_runner.DBRunner()
        self.get_passenger_info()
        self.register_passenger()

    def get_passenger_info(self):
        # Get Passenger information
        correct_info = False
        while not correct_info:
            self.first_name = input("Input passenger's first name: ")
            self.last_name = input("Input passenger's last name: ")
            self.passport_number = input("Input the passenger's passport number: ")
            self.ticket_number = input("Input passenger's ticket number: ")
            self.flight_id = int(input("Input the flight ID: "))
            print("Name:", self.first_name, "| Last Name:", self.last_name, "| Ticket.no:", self.ticket_number,
                  "| Passport.no:", self.passport_number, "| Flight ID:", self.flight_id)
            check = input("Is the above information correct (Y/N)? ").upper()
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

    def register_passenger(self):
        # If the flight is full.
        if self.conn.is_flight_full(self.flight_id):
            print("Sorry, the flight is full.")
        # Check if the passenger is already on the selected flight.
        elif self.conn.is_passenger_on_flight(self.first_name, self.last_name, self.ticket_number,
                                              self.passport_number, self.flight_id):
            print("Sorry, the passenger is already assigned to this flight.")
        else:
            # Add the passenger and update the number of passengers for that flight.
            self.conn.register_passenger(self.first_name, self.last_name, self.ticket_number,
                                         self.passport_number, self.flight_id)
            self.conn.update_number_of_flight_passengers(self.flight_id)
            print("Passenger added to the flight successfully.")


if __name__ == "__main__":
    BookingManager()


