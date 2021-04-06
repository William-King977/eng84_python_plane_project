# Test for flight trip
from flight_trip import FlightTrip
import unittest
import pytest


class FlightTest(unittest.TestCase):

    destination = str("Spain")
    duration = int(100)
    origin = str("England")

    manage = FlightTrip(destination, duration, origin)

    def test_flight_destination(self):
        self.assertEqual(self.manage.destination, self.destination)

    def test_flight_duration(self):
        self.assertEqual(self.manage.duration, self.duration)

    def test_flight_origin(self):
        self.assertEqual(self.manage.origin, self.origin)

# def test_allocatePlane(self):
#     pass
#
# def test_changePlane(self):
#     pass
#
# def test_addPassenger(self):
#     pass
#
# def test_viewPassengers(self):
#     pass



