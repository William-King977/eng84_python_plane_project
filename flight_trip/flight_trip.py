# As an airport assistant,
# I want to be able to assign and/or change a plane in my flight_trip by inputting my password,
# so that I can handle the problem.


# while True:
#     password = input("Please enter your password to gain access to this airport assistant: ")
#     if password == "Qwerty":
#         print("Welcome")
#         break
#     else:
#         print("Incorrect password please try again")

class FlightTrip:
    def __init__(self, destination, duration, origin):
        self.destination = str(destination)
        self.duration = int(duration)
        self.origin = str(origin)

    def allocate_plane(self):
        pass

    def change_plane(self):
        pass

    def add_passenger(self):
        pass

    def view_passengers(self):
        pass

