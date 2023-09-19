import sqlite3 as SQLite


class SQLiteDatabaseHandler:
    connection = None
    cursor = None

    def __init__(self, db_reference="chatbot-memory.db"):
        self.db_reference = db_reference

    def establish_db_connection(self):
        print("[ CONNECTING TO THE SQLITE DATABASE]")
        try:
            self.connection = SQLite.connect(self.db_reference)
            print("[ SUCCESSFULLY CONNECTED TO THE SQLITE DATABASE]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
        finally:
            self.connection.close()

    def terminate_db_connection(self):
        print("[ CLOSING DATABASE CONNECTIONS ]")
        self.connection.close()
        print("[ SUCCESSFULLY CLOSED DATABASE CONNECTIONS ]")
