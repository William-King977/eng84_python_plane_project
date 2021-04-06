import unittest
import pytest
from passenger import Passenger
from staff import Staff


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


#class StaffTest(unittest.TestCase):
    #person2 = Staff("Sam", "Smith", "1234")


#print("Name:", person1.first_name, person1.last_name, "  Tax num:", person1.tax_number, "  Passport num:", person1.passport_number)
#print("Name:", person2.first_name, person2.last_name, "  Tax num:", person2.tax_number)
