# This file is only used for creating the tables for the database.
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
    TaxNumber CHARACTER(8) NOT NULL
);
""")

# Staff table
conn.execute("""
CREATE TABLE IF NOT EXISTS Staff (
    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    TaxNumber CHARACTER(8) NOT NULL,
    Password CHARACTER(50) NOT NULL
);
""")

# Aircraft table
conn.execute("""
CREATE TABLE IF NOT EXISTS Aircraft (
    AircraftID INTEGER PRIMARY KEY AUTOINCREMENT,
    Model VARCHAR(30) NOT NULL,
    AircraftType VARCHAR(30) NOT NULL
);
""")

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