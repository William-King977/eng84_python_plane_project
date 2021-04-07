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



if __name__ == "__main__":
    runner = DBRunner()
    print(runner.get_flight_passengers(1))
