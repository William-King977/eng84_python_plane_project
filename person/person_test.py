import unittest
import pytest
from passenger import Passenger
from staff import Staff


# Test passenger
class PassengerTest(unittest.TestCase):
    first_name = "Bob"
    last_name = "Davis"
    ticket_number = "1233"
    passport_number = "0123"
    manage = Passenger(first_name, last_name, ticket_number, passport_number)

    def test_first_name(self):
        self.assertEqual(self.manage.first_name, self.first_name)

    def test_last_name(self):
        self.assertEqual(self.manage.last_name, self.last_name)

    def test_ticket_number(self):
        self.assertEqual(self.manage.ticket_number, self.ticket_number)

    def test_passport_number(self):
        self.assertEqual(self.manage.passport_number, self.passport_number)


# Test staff
class StaffTest(unittest.TestCase):
    first_name = "Bob"
    last_name = "Davis"
    username = "BDavis"
    password = "password123"
    manage = Staff(first_name, last_name, username, password)

    def test_first_name(self):
        self.assertEqual(self.manage.first_name, self.first_name)

    def test_last_name(self):
        self.assertEqual(self.manage.last_name, self.last_name)

    def test_username(self):
        self.assertEqual(self.manage.username, self.username)

    def test_password(self):
        self.assertEqual(self.manage.password, self.password)
