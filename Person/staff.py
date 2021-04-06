from person import Person


class Staff(Person):
    def __init__(self, first_name, last_name, tax_number):
        super().__init__(first_name, last_name, tax_number)
        self.password = "Passw0rd2018"
