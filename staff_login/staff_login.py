from local_db import db_runner


def login():
    # Only allow three attempts
    for i in range(3):
        username = input("Username: ")
        password = input("Password: ")

        conn = db_runner.DBRunner()
        if conn.check_staff_login(username, password):
            print("Login Successful.")
            break
        else:
            print("The username or password you have entered is incorrect.")
            if i == 2:
                print("Too many attempts, exiting program.")
                exit()
