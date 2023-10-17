import sqlite3 as SQLite
import SQLiteHandlerTemperatureCommand
import SQLiteHandlerHumidityCommand
import SQLiteHandlerUserCommand


class SQLiteDatabaseHandler:
    connection = None
    cursor = None

    def __init__(self, db_reference="chatbot-memory.db"):
        self.db_reference = db_reference
        self.temperature_handler = SQLiteHandlerTemperatureCommand()
        self.humidity_handler = SQLiteHandlerHumidityCommand()
        self.user_handler = SQLiteHandlerUserCommand()

    def establish_db_connection(self):
        """
        This function is used to establish a connection to the sqlite database.
        """
        print("[ CONNECTING TO THE SQLITE DATABASE]")
        try:
            self.connection = SQLite.connect(self.db_reference)
            self.cursor = self.connection.cursor()
            print("[ SUCCESSFULLY CONNECTED TO THE SQLITE DATABASE]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def terminate_db_connection(self):
        """
        This function terminates the database and cursor connection
        """
        print("[ CLOSING DATABASE CONNECTIONS ]")
        self.cursor.close()
        self.connection.close()
        print("[ SUCCESSFULLY CLOSED DATABASE CONNECTIONS ]")
