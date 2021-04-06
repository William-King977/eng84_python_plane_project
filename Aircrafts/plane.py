from aircraft import Aircraft

class Plane(Aircraft):
    def __init__(self, aircraft_id, flight_capacity, model):
        super().__init__(aircraft_id, flight_capacity)
        self.model = model