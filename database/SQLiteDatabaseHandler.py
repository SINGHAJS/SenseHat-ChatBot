import sqlite3 as SQLite


class SQLiteDatabaseHandler:
    connection = None
    cursor = None

    def __init__(self, db_reference="chatbot-memory.db"):
        self.db_reference = db_reference

    # This function is used to establish a connection to the sqlite database
    def establish_db_connection(self):
        print("[ CONNECTING TO THE SQLITE DATABASE]")
        try:
            self.connection = SQLite.connect(self.db_reference)
            self.cursor = self.connection.cursor()
            print("[ SUCCESSFULLY CONNECTED TO THE SQLITE DATABASE]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.connection.close()
            self.cursor.close()

    # This function is used to create temperature table if it does not exist
    def create_temp_table(self):
        sqlite_table_creation_query = """CREATE TABLE IF NOT EXISTS temperature ( 
            Id INTEGER PRIMARY KEY, 
            Temperature REAL NOT NULL, 
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""

        # self.cursor = self.connection.cursor()  # Create a cursor object

        # Execute the table creation query
        self.cursor.execute(sqlite_table_creation_query)
        self.connection.commit()  # Commmit changes to the database
        print("[ TEMPERATURE TABLE CREATED ]")

    # This function is used to insert a new temperature reading into the temperature table
    def insert_into_temp_table(self, temperature):
        sqlite_table_insertion_query = f""" INSERT INTO temperature (Temperature) VALUES ({temperature}) """

        # Execute table insertion query
        self.cursor.execute(sqlite_table_insertion_query)
        self.connection.commit()  # Commit changes to the database
        print(f"[ INSERTED {temperature} INTO TEMPERATURE TABLE ]")

    # This function is used to get the temperature readings from the tamperature table in the database.
    # Once the results are retrieved, the functions returns the results.
    def get_temperature_readings(self):
        sqlite_table_get_query = """SELECT * FROM temperature"""

        # Execute table retreival query
        self.cursor.execute(sqlite_table_get_query)
        query_response = self.cursor.fetchall()  # Fetch all the results
        print(query_response)

        return query_response  # Return the temperature results

    # This function is used create humidity table if it does not exist
    def create_humidity_table(self):
        sqlite_table_creation_query = """CREATE TABLE IF NOT EXISTS humidity ( 
            Id INTEGER PRIMARY KEY, 
            Humidity REAL NOT NULL, 
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""

        # self.cursor = self.connection.cursor()  # Create a cursor object

        # Execute the table creation query
        self.cursor.execute(sqlite_table_creation_query)
        self.connection.commit()  # Commmit changes to the database
        print("[ HUMIDITY TABLE CREATED ]")

    # This function is used to insert a new humidity reading into the humidity table
    def insert_into_humidity_table(self, humidity):
        sqlite_table_insertion_query = f""" INSERT INTO humidity (Humidity) VALUES ({humidity}) """

        # Execute table insertion query
        self.cursor.execute(sqlite_table_insertion_query)
        self.connection.commit()  # Commit changes to the database
        print(f"[ INSERTED {humidity} INTO HUMIDITY TABLE ]")

    # This function is used to get the humidity readings from the humidity table in the database.
    # Once the results are retrieved, the functions returns the results.
    def get_humidity_readings(self):
        sqlite_table_get_query = """SELECT * FROM humidity"""

        # Execute table retreival query
        self.cursor.execute(sqlite_table_get_query)
        query_response = self.cursor.fetchall()  # Fetch all the results
        print(query_response)

        return query_response  # Return the temperature results

    def terminate_db_connection(self):
        print("[ CLOSING DATABASE CONNECTIONS ]")
        self.connection.close()
        print("[ SUCCESSFULLY CLOSED DATABASE CONNECTIONS ]")
