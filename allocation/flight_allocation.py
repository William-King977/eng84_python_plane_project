from user_prompt import passenger_registration
from local_db import db_runner
from prettytable import PrettyTable
from allocation import flight_manager

conn = db_runner.DBRunner()


def manage_flights():
    f_manager = flight_manager.FlightManager()
    while True:
        plane_option = input("-= Flight Management =-\n"
                             "Select one of the options\n"
                             "1. Create a new flight\n"
                             "2. Display all available flights\n"
                             "3. Display all planes\n"
                             "4. Allocate/change a plane for a flight\n"
                             "5. Go back\n"
                             "=> ")
        if plane_option == "1":
            print("Creating a new flight")
            f_manager.create_new_flight()
        elif plane_option == "2":
            print("All available flights:")
            f_manager.display_available_flights()
        elif plane_option == "3":
            print("All active planes:")
            f_manager.display_all_planes()
        elif plane_option == "4":
            print("Allocating plane to a flight")
            f_manager.allocate_plane()
        elif plane_option == "5":
            print("Exiting flight management.")
            break
        else:
            print("Invalid option, please enter again.")


def assign_passengers():
    while True:
        enter_passenger = input("Do you want to assign a passenger (Y/N)? ").upper()
        if enter_passenger in ["YES", "TRUE", "T", "Y"]:
            passenger_registration.BookingManager()
        else:
            break


def display_flight_passengers():
    flight_id = int(input("Enter the flight ID for the flight: "))
    flight_passengers = conn.get_flight_passengers(flight_id)

    if len(flight_passengers) == 0:
        print("No passengers for that flight.")
    else:
        passenger_table = PrettyTable(["First Name", "Last Name", "Passport Number"])
        for passenger in flight_passengers:
            passenger_table.add_row(passenger)
        print(passenger_table)
    input("Press enter to continue.")


def main_menu():
    while True:
        allocation_choice = input("-= flight allocation =-\n"
                                  "Select one of the options\n"
                                  "1. Manage Flights\n"
                                  "2. Control for Passenger Allocation\n"
                                  "3. Display Passengers for a flight\n"
                                  "4. Log out\n"
                                  "=> ")
        if allocation_choice == "1":
            print("Flight Management")
            manage_flights()
        elif allocation_choice == "2":
            print("Passenger Allocation For Flights")
            assign_passengers()
        elif allocation_choice == "3":
            print("Display Passengers for a Flight")
            display_flight_passengers()
        elif allocation_choice == "4":
            print("Logging out.")
            break
        else:
            print("Invalid option, please enter again.")
