# Test cases for the db_runner.py queries.
# Mainly testing their return type.

# NOTE: Change directory to local_db before running test!
# Otherwise, it will run the wrong database.
from local_db.db_runner import DBRunner
import pytest
import unittest


class TestDBRunner(unittest.TestCase):
    db_obj = DBRunner()

    def test_get_all_passengers(self):
        self.assertEqual(type(self.db_obj.get_all_passengers()), list)

    def test_get_flight_passengers(self):
        self.assertEqual(type(self.db_obj.get_flight_passengers(1)), list)

    def test_get_all_flights(self):
        self.assertEqual(type(self.db_obj.get_all_flights()), list)

    def test_get_available_flights(self):
        self.assertEqual(type(self.db_obj.get_available_flights()), list)

    def test_get_all_planes(self):
        self.assertEqual(type(self.db_obj.get_all_planes()), list)




