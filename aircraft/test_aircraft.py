import unittest
import pytest
from aircraft import Aircraft
from plane import Plane

# Test Aircraft
class MyTestCase(unittest.TestCase):
    aircraft_id = "1"
    flight_capacity = int(100)
    air = Aircraft(aircraft_id, flight_capacity)

    def test_aircraft_id(self):
        self.assertEqual(self.air.aircraft_id, self.aircraft_id)

    def test_flight_capacity(self):
        self.assertEqual(self.air.flight_capacity, self.flight_capacity)


# Test Plane
class PlaneTest(unittest.TestCase):
    aircraft_id = "1"
    flight_capacity = int(100)
    model = ""
    pl = Plane(aircraft_id, flight_capacity, model)

    def test_aircraft_id(self):
        self.assertEqual(self.pl.aircraft_id, self.aircraft_id)

    def test_flight_capacity(self):
        self.assertEqual(self.pl.flight_capacity, self.flight_capacity)

    def test_model(self):
        self.assertEqual(self.pl.model, self.model)

if __name__ == '__main__':
    unittest.main()



# python -m unittest discover -v
# python -m pytest




