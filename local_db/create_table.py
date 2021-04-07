# This file is only used for creating the tables for the database
# as well as inserting fake data into the tables.
import sqlite3

# Establish a connection with the DB
conn = sqlite3.connect("PlaneProjectDB.db")

# Passengers table
conn.execute("""
CREATE TABLE IF NOT EXISTS Passengers (
    PassengerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    PassportNumber CHARACTER(9) NOT NULL,
    TaxNumber VARCHAR(10) NOT NULL
);
""")

# Insert Passengers
# conn.execute("""
# INSERT INTO Passengers
# (FirstName, LastName, PassportNumber, TaxNumber)
# VALUES
# ('William', 'King', '123456789', '99L99999'),
# ('Brian', 'Burke', '987654321', '12Q34567'),
# ('Sarah', 'Shaw', '543216789', '98B76543')
# """)


# Staff table
conn.execute("""
CREATE TABLE IF NOT EXISTS Staff (
    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    TaxNumber CHARACTER(8) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
);
""")

# Insert Staff
# conn.execute("""
# INSERT INTO Staff
# (FirstName, LastName, TaxNumber, Username, Password)
# VALUES
# ('William', 'King', '98F12345', 'KingBigW', 'password123')
# """)


# Aircraft table
conn.execute("""
CREATE TABLE IF NOT EXISTS Aircraft (
    AircraftID INTEGER PRIMARY KEY AUTOINCREMENT,
    Model VARCHAR(30) NOT NULL,
    AircraftType VARCHAR(30) NOT NULL,
    FlightCapacity INTEGER NOT NULL
);
""")

# Insert Aircraft
# conn.execute("""
# INSERT INTO Aircraft
# (Model, AircraftType, FlightCapacity)
# VALUES
# ('Boeing 777', 'Plane', 100),
# ('Airbus A320', 'Plane', 100)
# """)


# Flights table
conn.execute("""
CREATE TABLE IF NOT EXISTS Flights (
    FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
    AircraftID INTEGER,
    Origin VARCHAR(30) NOT NULL,
    Destination VARCHAR(30) NOT NULL,
    Duration INTEGER NOT NULL,
    DepartureDate DATE NOT NULL,
    DepartureTime TIME NOT NULL,
    ArrivalDate DATE NOT NULL,
    ArrivalTime TIME NOT NULL,
    FOREIGN KEY(AircraftID) REFERENCES Aircraft(AircraftID)
);
""")

# Bookings table
conn.execute("""
CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
    FlightID INTEGER NOT NULL,
    PassengerID INTEGER NOT NULL,
    BookingDate DATE NOT NULL,
    BookingTime TIME NOT NULL,
    FOREIGN KEY(FlightID) REFERENCES Flights(FlightID),
    FOREIGN KEY(PassengerID) REFERENCES Passengers(PassengerID)
);
""")

# Apply the changes
conn.commit()

# Always close the connection
conn.close()