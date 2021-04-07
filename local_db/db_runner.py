# This class holds all the methods that executes the appropriate queries
# on the local database.
import sqlite3


class DBRunner:
    def __init__(self):
        self.conn = sqlite3.connect("PlaneProjectDB.db")

    # Close the connection.
    def __del__(self):
        self.conn.close()

    # Gets every registered passenger
    def get_all_passengers(self):
        # fetchall() returns a list of tuples.
        return self.conn.execute("SELECT * FROM Passengers;").fetchall()

    # Gets every passenger for a particular flight
    def get_flight_passengers(self, flight_id):
        result = self.conn.execute(f"SELECT * FROM Passengers p INNER JOIN Bookings b "
                                   f"ON p.PassengerID = b.PassengerID "
                                   f"WHERE b.FlightID = {flight_id};").fetchall()
        return result

    # Gets every flight
    def get_all_flights(self):
        return self.conn.execute("SELECT * FROM Flights;").fetchall()

    # Gets flights with a departure date of today or later
    def get_available_flights(self):
        # Date format is dd/mm/YYYY
        result = self.conn.execute("SELECT * FROM Flights "
                                   "WHERE DepartureDate >= strftime('%d/%m/%Y','now');").fetchall()
        return result

    # Adds a new staff member to the system.
    def register_staff(self, first_name, last_name, tax_number, username, password):
        self.conn.execute(f"INSERT INTO Staff "
                          f"(FirstName, LastName, TaxNumber, Username, Password) "
                          f"VALUES "
                          f"({first_name}, {last_name}, {tax_number}, {username}, {password});")
        # Save the changes.
        self.conn.commit()

    # Checks if a staff's login details are correct
    def check_staff_login(self, username, password):
        staff_member = self.conn.execute(f"SELECT * FROM Staff "
                                         f"WHERE Username = {username};").fetchone()
        return staff_member[0][5] == password

    # Adds a passenger to a flight with their details
    def register_passenger(self, first_name, last_name, tax_number, passport_number, flight_id):
        self.conn.execute(f"INSERT INTO Passengers "
                          f"(FirstName, LastName, TaxNumber, PassportNumber) "
                          f"VALUES "
                          f"({first_name}, {last_name}, {tax_number}, {passport_number});")
        self.conn.commit()
        new_passenger_id = self.conn.execute("SELECT PassengerID FROM Passengers").fetchone()[0][0]
        self.__create_booking(new_passenger_id, flight_id)

    # Creates a booking for the added passenger
    def __create_booking(self, passenger_id, flight_id):
        self.conn.execute(f"INSERT INTO Bookings "
                          f"(FlightID, PassengerID, BookingDate, BookingTime) "
                          f"VALUES "
                          f"({flight_id}, {passenger_id}, strftime('%d/%m/%Y','now'), "
                          f"strftime('%H:%M','now'));")
        self.conn.commit()

    # Creates a new flight
    def create_flight(self, aircraft_id, origin, destination, duration, departure_date,
                      departure_time, arrival_date, arrival_time):
        self.conn.execute(f"INSERT INTO Flights "
                          f"(AircraftID, Origin, Destination, Duration, DepartureDate, "
                          f"DepartureTime, ArrivalDate, ArrivalTime) "
                          f"VALUES "
                          f"({aircraft_id}, {origin}, {destination}, {duration}, {departure_date}, "
                          f"{departure_time}, {arrival_date}, {arrival_time});")
        self.conn.commit()

    # Allows a staff member to allocate a plane to a flight
    def add_aircraft_to_flight(self, flight_id, aircraft_id):
        self.conn.execute(f"UPDATE Flights "
                          f"SET AircraftID = {aircraft_id} "
                          f"WHERE FlightID = {flight_id};")
        self.conn.commit()


if __name__ == "__main__":
    runner = DBRunner()
    print(runner.get_flight_passengers(1))
    print(runner.get_available_flights())
    print(runner.conn.execute("SELECT * FROM Passengers").fetchall()[0][0])
