from user_prompt import passenger_registration
from local_db import db_runner

conn = db_runner.DBRunner()


def plane_allocation():
    for i in range(3):
        password = input("Enter password")
        if password == "password":
            plane_option = input("-= Plane Management =-\n"
                                 "Select one of the options\n"
                                 "1. Display all planes\n"
                                 "2. Allocate/change a plane for a flight\n"
                                 "3. Go back\n"
                                 "=> ")
            if plane_option == "1":
                print("ALL ACTIVE PLANES")
            elif plane_option == "2":
                print("Enter the flight ID of the flight to modify: ")
            elif plane_option == "3":
                print("Exiting plane management.")
                break
            else:
                print("Invalid option, please enter again.")
        else:
            print("Incorrect Password, please try again.")
            if i == 2:
                print("Too many attempts, access denied.")
                break


def assign_passengers():
    while True:
        enter_passenger = input("Do you want to assign a passenger (Y/N)? ").upper()
        if enter_passenger in ["YES", "TRUE", "T", "Y"]:
            passenger_registration.BookingManager()
        else:
            break


def display_available_flights():
    available_flights = conn.get_available_flights()
    if len(available_flights) == 0:
        print("No flights are currently available.")
    else:
        for flight in available_flights:
            print(f"""Flight ID:      {flight[0]}
                      Origin:         {flight[1]}
                      Destination:    {flight[2]}
                      Duration:       {flight[3]}
                      Departure Date: {flight[4]}
                      Departure Time: {flight[5]}
                      Arrival Date:   {flight[6]}
                      Arrival Time:   {flight[7]} \n
                   """)


def main_menu():
    while True:
        allocation_choice = input("-= flight allocation =-\n"
                                  "Select one of the options\n"
                                  "1. Control for Plane Allocation\n"
                                  "2. Control for Passenger Allocation \n"
                                  "3. Create a new flight\n"
                                  "4. Display available flights\n"
                                  "5. Log out\n"
                                  "=> ")
        if allocation_choice == "1":
            print("PLANE ALLOCATION FOR FLIGHTS ")
            plane_allocation()
        elif allocation_choice == "2":
            print("PASSENGER ALLOCATION FOR FLIGHTS ")
            assign_passengers()
        elif allocation_choice == "3":
            print("CREATE A NEW FLIGHT")
        elif allocation_choice == "4":
            print("AVAILABLE FLIGHTS")
            display_available_flights()
        elif allocation_choice == "5":
            print("Logging out.")
            break
        else:
            print("Invalid option, please enter again.")
