###################################################################################
def passenger_management():
    flight = []
    while True:
        passengerOnFlight = input("Add Passengers name to flight  ")
        flight.append(passengerOnFlight)
        print(f"{flight} is on the flight")
        break
################################################################################
def plane_allocation():
    while True:
        password = input("Enter password")
        if password == "password":
            planeDecision = input("-= Flight Management =-\n"
                                  "Select one of the options\n"
                                  "1. Allocate a Plane\n"
                                  "2. Change a Plane\n"
                                  "3. Edit or Update flight table\n"
                                  "4. Go back\n"
                                  "=> ")
            if planeDecision.isdigit():
                planeDecision = int(planeDecision)
                if planeDecision == 1:
                    print("Enter plane details to add")
                    break
                elif planeDecision == 2:
                    print("Enter plane details to remove")
                    break
                elif planeDecision == 3:
                    print("Enter the plane details to edit")
                    break
                elif planeDecision == 4:
                    print("Exiting Program now")
                    break
                else:
                    print("Invalid input")
                    break
            else:
                print("invalid input")
        else:
            print("Incorrect Password, please try again ! ")
###########################################################################################
while True:
    allocation_choice = input("-= flight allocation =-\n"
                              "Select one of the options\n"
                              "1. Control for Plane Allocation\n"
                              "2. Control for Passenger Allocation \n"
                              "3. exit\n"
                              "=> ")
    if allocation_choice == "1":
        print("PLANE ALLOCATION FOR FLIGHTS ")
        plane_allocation()

    elif allocation_choice == "2":
        print("PASSENGER ALLOCATION FOR FLIGHTS ")
        passenger_management()

    elif allocation_choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid option, please enter again.")