import sqlite3


class DBRunner:
    def __init__(self):
        self.conn = sqlite3.connect("PlaneProjectDB.db")

    # Close the connection.
    def __del__(self):
        self.conn.close()
