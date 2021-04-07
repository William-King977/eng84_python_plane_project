from person.person import Person


class Staff(Person):
    def __init__(self, first_name, last_name, tax_number, username, password):
        super().__init__(first_name, last_name, tax_number)
        self.username = username
        self.password = password
