import unittest
import pytest
from person.passenger import Passenger
from person.staff import Staff


# Test passenger
class PassengerTest(unittest.TestCase):
    first_name = "Bob"
    last_name = "Davis"
    tax_number = "1233"
    passport_number = "0123"
    manage = Passenger(first_name, last_name, tax_number, passport_number)

    def test_first_name(self):
        self.assertEqual(self.manage.first_name, self.first_name)

    def test_last_name(self):
        self.assertEqual(self.manage.last_name, self.last_name)

    def test_tax_number(self):
        self.assertEqual(self.manage.tax_number, self.tax_number)

    def test_passport_number(self):
        self.assertEqual(self.manage.passport_number, self.passport_number)


# Test staff
class StaffTest(unittest.TestCase):
    first_name = "Bob"
    last_name = "Davis"
    tax_number = "1233"
    manage = Staff(first_name, last_name, tax_number)

    def test_first_name(self):
        self.assertEqual(self.manage.first_name, self.first_name)

    def test_last_name(self):
        self.assertEqual(self.manage.last_name, self.last_name)

    def test_tax_number(self):
        self.assertEqual(self.manage.tax_number, self.tax_number)
