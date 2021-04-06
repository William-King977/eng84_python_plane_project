# As an airport assistant,
# I want to be able to assign and/or change a plane in my flight_trip by inputting my password,
# so that I can handle the problem.


# while True:
#     passWord = input("Please enter your password to gain access to this ait port assistant: ")
#     if passWord == "Qwerty":
#         print("Welcome")
#         break
#     else:
#         print("Incorrect password please try again")

class FlightTrip:
    def __init__(self, destination, duration, origin):
        self.destination = str(destination)
        self.duration = int(duration)
        self.origin = str(origin)

    def allocatePlane(self):
        pass

    def changePlane(self):
        pass

    def addPassenger(self):
        pass

    def viewPassengers(self):
        pass

