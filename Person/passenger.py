from person import Person


class Passenger(Person):
    def __init__(self, first_name, last_name, tax_number, passport_number):
        super().__init__(first_name, last_name, tax_number)
        self.passport_number = passport_number
