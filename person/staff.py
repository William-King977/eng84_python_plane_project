from person.person import Person


class Staff(Person):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name)
        self.username = username
        self.password = password
