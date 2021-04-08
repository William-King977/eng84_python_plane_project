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

    # Sets the password for the currently logged in staff member.
    def set_curr_password(self, password):
        # Delete the table row first.
        self.cursor.execute("DELETE FROM CurrentPassword;")
        self.cursor.execute(f"INSERT INTO CurrentPassword "
                            f"(Password) "
                            f"VALUES "
                            f"('{password}');")
        self.conn.commit()

    # Gets the password of the currently logged in staff member.
    def get_curr_password(self):
        return self.cursor.execute("SELECT Password FROM CurrentPassword;").fetchone()[0]

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
                            f"DepartureTime, ArrivalDate, ArrivalTime, NumberOfPassengers) "
                            f"VALUES "
                            f"({aircraft_id}, '{origin}', '{destination}', '{duration}', '{departure_date}', "
                            f"'{departure_time}', '{arrival_date}', '{arrival_time}' , 0);")
        self.conn.commit()

    # Allows a staff member to allocate a plane to a flight
    def add_aircraft_to_flight(self, flight_id, aircraft_id):
        self.cursor.execute(f"UPDATE Flights "
                            f"SET AircraftID = {aircraft_id} "
                            f"WHERE FlightID = {flight_id};")
        self.conn.commit()

    # Increments the number of passengers on a flight by 1.
    def update_number_of_flight_passengers(self, flight_id):
        self.cursor.execute(f"UPDATE Flights "
                            f"SET NumberOfPassengers = NumberOfPassengers + 1 "
                            f"WHERE FlightID = {flight_id};")
        self.conn.commit()

    # Checks if a flight is fully booked.
    def is_flight_full(self, flight_id):
        flight = self.cursor.execute(f"SELECT AircraftID, NumberOfPassengers FROM Flights "
                                     f"WHERE FlightID = {flight_id};").fetchone()

        aircraft_id = flight[0]
        num_passengers = flight[1]
        plane_capacity = self.cursor.execute(f"SELECT FlightCapacity FROM Aircraft "
                                             f"WHERE AircraftID = {aircraft_id};").fetchone()[0]
        return num_passengers >= plane_capacity

    # Checks if a passenger is already on a flight.
    def is_passenger_on_flight(self, first_name, last_name, ticket_number, passport_number, flight_id):
        result = self.cursor.execute(f"SELECT * "
                                     f"FROM Passengers p INNER JOIN Bookings b "
                                     f"ON p.PassengerID = b.PassengerID "
                                     f"WHERE p.FirstName = '{first_name}' AND "
                                     f"p.LastName = '{last_name}' AND "
                                     f"p.TicketNumber = '{ticket_number}' AND "
                                     f"p.PassportNumber = '{passport_number}' AND "
                                     f"b.FlightID = {flight_id};").fetchone()
        return result is not None


if __name__ == "__main__":
    runner = DBRunner()
    print(runner.get_flight_passengers(1))
    print(runner.get_available_flights())
    print(runner.conn.execute("SELECT * FROM Passengers").fetchall())
    print(runner.conn.execute("SELECT * FROM Bookings").fetchall())
    print(runner.check_staff_login("KingBigW", "Password123"))
