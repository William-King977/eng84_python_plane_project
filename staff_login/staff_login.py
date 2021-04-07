from local_db import db_runner


def staff_login():
    while True:
        username = input("Username:    ")
        password = input("Password:    ")

        db_query = db_runner.DBRunner()
        if db_query.check_staff_login(username, password):
            print("Login Successful.")
            break
        else:
            print("The username or password you have entered is incorrect.")
