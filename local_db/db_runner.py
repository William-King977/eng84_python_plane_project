# This class holds all the methods that executes the appropriate queries
# on the local database.
import sqlite3
import os
from pathlib import Path


class DBRunner:
    def __init__(self):
        self.start_connection()

    # Close the connection.
    def __del__(self):
        self.conn.close()

    # Initialises the connection
    def start_connection(self):
        # Changes the directory back to "here", regardless of where
        # this class is called.
        curr_path = Path(os.getcwd())
        project_path = curr_path.parent

        # Test the connection
        try:
            self.conn = sqlite3.connect(fr"{project_path}\local_db\PlaneProjectDB.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Failed to connect: {error}.")

    # Gets every registered passenger
    def get_all_passengers(self):
        # fetchall() returns a list of tuples.
        return self.cursor.execute("SELECT * FROM Passengers;").fetchall()

    # Gets every passenger for a particular flight
    def get_flight_passengers(self, flight_id):
        result = self.cursor.execute(f"SELECT p.FirstName, p.LastName, p.PassportNumber "
                                     f"FROM Passengers p INNER JOIN Bookings b "
                                     f"ON p.PassengerID = b.PassengerID "
                                     f"WHERE b.FlightID = {flight_id};").fetchall()
        return result

    # Gets every flight
    def get_all_flights(self):
        return self.cursor.execute("SELECT * FROM Flights;").fetchall()

    # Gets flights with a departure date of today or later
    def get_available_flights(self):
        # Date format is dd/mm/YYYY
        result = self.cursor.execute("SELECT * FROM Flights "
                                     "WHERE DepartureDate >= strftime('%d/%m/%Y','now');").fetchall()
        return result

    # Gets all of the planes
    def get_all_planes(self):
        result = self.cursor.execute("SELECT AircraftID, Model, FlightCapacity "
                                     "FROM Aircraft "
                                     "WHERE AircraftType = 'Plane';").fetchall()
        return result

    # Adds a new staff member to the system.
    def register_staff(self, first_name, last_name, username, password):
        self.cursor.execute(f"INSERT INTO Staff "
                            f"(FirstName, LastName, Username, Password) "
                            f"VALUES "
                            f"('{first_name}', '{last_name}', '{username}', '{password}');")
        # Save the changes.
        self.conn.commit()

    # Checks if a staff's login details are correct
    def check_staff_login(self, username, password):
        staff_member = self.cursor.execute(f"SELECT * FROM Staff "
                                           f"WHERE Username = '{username}';").fetchone()
        # Check if the username exists first.
        if staff_member is None:
            return False

        # Then check the password.
        return staff_member[4] == password

    # Adds a passenger to a flight with their details
    def register_passenger(self, first_name, last_name, ticket_number, passport_number, flight_id):
        self.cursor.execute(f"INSERT INTO Passengers "
                            f"(FirstName, LastName, TicketNumber, PassportNumber) "
                            f"VALUES "
                            f"('{first_name}', '{last_name}', '{ticket_number}', '{passport_number}');")
        self.conn.commit()
        new_passenger_id = self.cursor.execute(f"SELECT PassengerID FROM Passengers "
                                               f"WHERE FirstName = '{first_name}' AND "
                                               f"LastName = '{last_name}' AND "
                                               f"TicketNumber = '{ticket_number}' AND "
                                               f"PassportNumber = '{passport_number}'").fetchone()[0]
        self.__create_booking(new_passenger_id, flight_id)

    # Creates a booking for the added passenger
    def __create_booking(self, passenger_id, flight_id):
        self.cursor.execute(f"INSERT INTO Bookings "
                            f"(FlightID, PassengerID, BookingDate, BookingTime) "
                            f"VALUES "
                            f"({flight_id}, {passenger_id}, strftime('%d/%m/%Y','now'), "
                            f"strftime('%H:%M','now'));")
        self.conn.commit()

    # Creates a new flight
    def create_flight(self, aircraft_id, origin, destination, duration, departure_date,
                      departure_time, arrival_date, arrival_time):
        self.cursor.execute(f"INSERT INTO Flights "
                            f"(AircraftID, Origin, Destination, Duration, DepartureDate, "
                            f"DepartureTime, ArrivalDate, ArrivalTime) "
                            f"VALUES "
                            f"({aircraft_id}, '{origin}', '{destination}', '{duration}', '{departure_date}', "
                            f"'{departure_time}', '{arrival_date}', '{arrival_time}');")
        self.conn.commit()

    # Allows a staff member to allocate a plane to a flight
    def add_aircraft_to_flight(self, flight_id, aircraft_id):
        self.cursor.execute(f"UPDATE Flights "
                            f"SET AircraftID = {aircraft_id} "
                            f"WHERE FlightID = {flight_id};")
        self.conn.commit()


if __name__ == "__main__":
    runner = DBRunner()
    print(runner.get_flight_passengers(1))
    print(runner.get_available_flights())
    print(runner.conn.execute("SELECT * FROM Passengers").fetchall())
    print(runner.conn.execute("SELECT * FROM Bookings").fetchall())
    print(runner.check_staff_login("KingBigW", "Password123"))

    # [(1, 1, 'Heathrow', 'Palma', 180, '11/04/2021', '13:00', '11/04/2021', '16:00'),
    #  (2, 1, 'Dublin', 'Paris', 120, '15/04/2021', '23:00', '16/04/2021', '01:00')]
    # [(1, 'Chris', 'Wilson', '1234', '12345678'), (2, 'Brian', 'Burke', '98765', '98765432'),
    #  (3, 'Sarah', 'Shaw', '57493', '57493901')]
    # [(1, 1, 1, '08/04/2021', '08:14'), (2, 1, 2, '08/04/2021', '08:15'), (3, 2, 3, '08/04/2021', '08:15')]
