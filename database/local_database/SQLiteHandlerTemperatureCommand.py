import SQLiteDatabaseHandler
import sqlite3 as SQLite


class SQLiteHandlerTemperatureCommand(SQLiteDatabaseHandler):
    def create_temp_table(self):
        """
        This function is used to create temperature table if it does not exist.
        """
        sqlite_table_creation_query = """CREATE TABLE IF NOT EXISTS temperature ( 
            Id INTEGER PRIMARY KEY, 
            Temperature REAL NOT NULL, 
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""  # Temperature table creation query

        try:
            # Execute the table creation query
            self.cursor.execute(sqlite_table_creation_query)
            self.connection.commit()  # Commmit changes to the database
            print("[ TEMPERATURE TABLE CREATED ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def insert_into_temp_table(self, temperature):
        """
        This function is used to insert a new temperature reading into the temperature table.
        :param temperature: int, temperature
        """
        # Temperature table insertion query
        sqlite_table_insertion_query = f""" INSERT INTO temperature (Temperature) VALUES (?) """

        try:
            # Execute table insertion query
            self.cursor.execute(sqlite_table_insertion_query, (temperature,))
            self.connection.commit()  # Commit changes to the database
            print(f"[ INSERTED {temperature} INTO TEMPERATURE TABLE ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def get_temperature_readings(self):
        """
        This function is used to get the temperature readings from the tamperature table in the database. 
        Once the results are retrieved, the functions returns the results.

        :return: list of temperature readings
        """
        sqlite_table_get_query = """SELECT * FROM temperature"""  # Temperature values retrieval query

        try:
            # Execute table retreival query
            self.cursor.execute(sqlite_table_get_query)
            query_response = self.cursor.fetchall()  # Fetch all the results
            print(query_response)
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        return query_response if len(query_response) > 0 else 'No data entry avaliable!'

    def get_temperature_reading_at_time(self, time):
        """
        This function is used to get the temperature readings based on the given time. 
        :param time: str, time

        :return: list of temperature if match, otherwise 'No database entry found!'
        """
        sqlite_table_where_query = """ SELECT Temperature
                                       FROM temperature
                                       WHERE Timestamp = ?"""

        try:
            query_response = self.cursor.execute(
                sqlite_table_where_query, (time,))  # Execute the query
            result = query_response.fetchall()  # Get all the results from the query
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the list of temperature if match, otherwise 'No database entry found!'
        return result if len(result) > 0 else 'No database entry found!'

    def get_time_reading_at_temperature(self, temperature):
        """
        This function is used to get the time at the given temperature. 
        :param temperature: int, temperature

        :return: list of temperature if match, otherwise 'No database entry found!'
        """
        sqlite_table_where_query = """ SELECT Timestamp
                                       FROM temperature
                                       WHERE Temperature = ?"""

        try:
            query_response = self.cursor.execute(
                sqlite_table_where_query, (temperature,))
            result = query_response.fetchall()
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the list of temperature if match, otherwise 'No database entry found!'
        return result if len(result) > 0 else 'No database entry found!'
