from local_db import db_runner
from prettytable import PrettyTable


class FlightManager:
    def __init__(self):
        self.conn = db_runner.DBRunner()

    def create_new_flight(self):
        correct_info = False
        while not correct_info:
            aircraft_id = int(input("Enter aircraft ID: "))
            origin = input("Enter the origin: ")
            destination = input("Enter the destination: ")
            duration = input("Enter the flight duration: ")
            departure_date = input("Enter the departure date: ")
            departure_time = input("Enter the departure time: ")
            arrival_date = input("Enter the arrival date: ")
            arrival_time = input("Enter the arrival time: ")
            print(f"Aircraft ID: {aircraft_id} | Origin: {origin} | Destination: {destination} \n"
                  f"Duration: {duration} | Departure Date: {departure_date} | Departure Time: {departure_time} \n"
                  f"Arrival Date: {arrival_date} | Arrival Time: {arrival_time}")
            check = input("Is the above information correct (Y/N)? ").upper()
            if check in ["YES", "TRUE", "T", "Y"]:
                correct_info = True

        # Insert the flight into the table
        self.conn.create_flight(aircraft_id, origin, destination, duration, departure_date,
                                departure_time, arrival_date, arrival_time)
        print("Flight created successfully.")

    def display_available_flights(self):
        available_flights = self.conn.get_available_flights()
        if len(available_flights) == 0:
            print("No flights are currently available.")
        else:
            flight_table = PrettyTable(["Flight ID", "Aircraft ID", "Origin", "Destination",
                                        "Duration", "Departure Date", "Departure Time",
                                        "Arrival Date", "Arrival Time"])
            for flight in available_flights:
                flight_table.add_row(flight)
            print(flight_table)
        input("Press enter to continue.")

    def display_all_planes(self):
        all_planes = self.conn.get_all_planes()
        if len(all_planes) == 0:
            print("No planes are available.")
        else:
            plane_table = PrettyTable(["Aircraft ID", "Model", "Capacity"])
            for plane in all_planes:
                plane_table.add_row(plane)
            print(plane_table)
        input("Press enter to continue.")

    def allocate_plane(self):
        # Get the staff's password
        staff_password = self.conn.get_curr_password()

        # Ask for a password
        for i in range(3):
            password = input("Enter password: ")
            if password == staff_password:
                flight_id = int(input("Enter the flight ID of the flight to modify: "))
                aircraft_id = int(input("Enter the aircraft ID of the plane: "))
                self.conn.add_aircraft_to_flight(flight_id, aircraft_id)
                print("Plane updated successfully.")
                break
            else:
                print("Incorrect Password, please try again.")
                if i == 2:
                    print("Too many attempts, access denied.")
                    break
