from user_prompt import passenger_registration
from local_db import db_runner
from prettytable import PrettyTable
from allocation import flight_manager

conn = db_runner.DBRunner()


def manage_flights():
    f_manager = flight_manager.FlightManager()
    while True:
        plane_option = input("== Flight Management ==\n"
                             "Select one of the options\n"
                             "1. Create a New Flight\n"
                             "2. Display all Available Flights\n"
                             "3. Display all Planes\n"
                             "4. Allocate/Change a Plane for a Flight\n"
                             "5. Go Back\n"
                             "=> ")
        if plane_option == "1":
            print("Creating a New Flight")
            f_manager.create_new_flight()
        elif plane_option == "2":
            print("All Available Flights:")
            f_manager.display_available_flights()
        elif plane_option == "3":
            print("All Active Planes:")
            f_manager.display_all_planes()
        elif plane_option == "4":
            print("Allocating a Plane to a Flight")
            f_manager.allocate_plane()
        elif plane_option == "5":
            print("Exiting Flight Management.")
            break
        else:
            print("Invalid option, please enter again.")


def manage_passenger_menu():
    p_manager = passenger_registration.BookingManager()
    while True:
        option = input("== Passenger Management ==\n"
                       "Select one of the options\n"
                       "1. Register a Passenger\n"
                       "2. Add Passenger to a Flight\n"
                       "3. Display all Passengers\n"
                       "4. Go Back\n"
                       "=> ")
        if option == "1":
            print("Passenger Registration")
            p_manager.get_passenger_info()
        elif option == "2":
            print("Allocate a Passenger to a Flight")
            p_manager.passenger_booking()
        elif option == "3":
            print("All Registered Passengers:")
            p_manager.display_all_passengers()
        elif option == "4":
            print("Exiting Passenger Management.")
            break
        else:
            print("Invalid option, please enter again.")


def display_flight_passengers():
    flight_id = int(input("Enter the flight ID for the flight: "))
    flight_passengers = conn.get_flight_passengers(flight_id)

    if len(flight_passengers) == 0:
        print("No passengers for that flight.")
    else:
        passenger_table = PrettyTable(["Passenger ID", "First Name", "Last Name", "Passport Number"])
        for passenger in flight_passengers:
            passenger_table.add_row(passenger)
        print(passenger_table)
    input("Press enter to continue.")


def main_menu():
    while True:
        allocation_choice = input("== Flight Allocation System ==\n"
                                  "Select one of the options\n"
                                  "1. Manage Flights\n"
                                  "2. Manage Passengers\n"
                                  "3. Display all Passengers for a Flight\n"
                                  "4. Log Out\n"
                                  "=> ")
        if allocation_choice == "1":
            print("Flight Management")
            manage_flights()
        elif allocation_choice == "2":
            print("Passenger Management For Flights")
            manage_passenger_menu()
        elif allocation_choice == "3":
            print("Display Passengers for a Flight")
            display_flight_passengers()
        elif allocation_choice == "4":
            print("Logging out.")
            break
        else:
            print("Invalid option, please enter again.")
