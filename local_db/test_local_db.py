# Test cases for the db_runner.py queries.
import db_runner
import unittest


class TestDBRunner(unittest.TestCase):
    db_obj = db_runner

    def test_get_all_passengers(self):
        self.assertEqual(self.db_obj.get_all_passengers(), not None)

    def test_get_flight_passengers(self):
        self.assertEqual(self.db_obj.get_flight_passengers(1), not None)





