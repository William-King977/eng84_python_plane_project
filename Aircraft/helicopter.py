import pyodbc
from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, aircraft_id, flight_capacity):
        super().__init__()