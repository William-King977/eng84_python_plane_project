# Runs the main program.
# Functionality is split into separate Python modules (.py files).
from staff_login import staff_login, register_staff

# Runs until the user wants to exit.
# The staff member is asked to login.
while True:
    user_option = input("Do you want to login or register? \n"
                        "1. Login \n"
                        "2. Register \n"
                        "3. Quit \n"
                        "Enter option here: ")
    if user_option == "1":
        # The user will be prompt to login.
        staff_login.login()

        continue
    elif user_option == "2":
        # The user will be prompt to register with their details.
        register_staff.RegisterStaff()

    elif user_option == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid option, please enter again.")
