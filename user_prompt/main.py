# Runs the main program.
# Functionality is split into separate Python modules (.py files).

# Runs until the user wants to exit.
while True:
    user_type = input("Are you a customer or staff member? (q to exit) ").lower()
    if user_type == "customer":
        # This print statement will be replaced with a function.
        print("Customer")
    elif user_type == "staff":
        # This print statement will be replaced with a function.
        print("Staff")
    elif user_type == "q":
        print("Exiting program.")
        break
    else:
        print("Invalid option, please enter again.")
