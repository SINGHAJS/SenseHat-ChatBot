import SQLiteDatabaseHandler
import sqlite3 as SQLite


class SQLiteHandlerTemperatureCommand(SQLiteDatabaseHandler):
    def create_humidity_table(self):
        """
        This function is used create humidity table if it does not exist
        """
        sqlite_table_creation_query = """CREATE TABLE IF NOT EXISTS humidity ( 
            Id INTEGER PRIMARY KEY, 
            Humidity REAL NOT NULL, 
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""  # Humidity table creation query

        try:
            # Execute the table creation query
            self.cursor.execute(sqlite_table_creation_query)
            self.connection.commit()  # Commmit changes to the database
            print("[ HUMIDITY TABLE CREATED ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def insert_into_humidity_table(self, humidity):
        """
        This function is used to insert a new humidity reading into the humidity table
        """
        # Humidity table insertion query
        sqlite_table_insertion_query = f""" INSERT INTO humidity (Humidity) VALUES (?) """

        try:
            # Execute table insertion query
            self.cursor.execute(sqlite_table_insertion_query, (humidity,))
            self.connection.commit()  # Commit changes to the database
            print(f"[ INSERTED {humidity} INTO HUMIDITY TABLE ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def get_humidity_readings(self):
        """
        This function is used to get the humidity readings from the humidity table in the database.
        Once the results are retrieved, the functions returns the results.

        :return: list of humidity readings
        """
        sqlite_table_get_query = """SELECT * FROM humidity"""  # Humidity values retrieval query

        try:
            # Execute table retreival query
            self.cursor.execute(sqlite_table_get_query)
            query_response = self.cursor.fetchall()  # Fetch all the results
            print(query_response)
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the humidity results
        return query_response if len(query_response) > 0 else 'No data entry avaliable!'

    def get_humidity_reading_at_time(self, time):
        """
        This function is used to get the humidity readings based on the given time. 
        :param time: str, time

        :return: list of humidity if match, otherwise 'No database entry found!'
        """
        sqlite_table_where_query = """ SELECT Humidity
                                       FROM humidity
                                       WHERE Timestamp = ?"""

        try:
            query_response = self.cursor.execute(
                sqlite_table_where_query, (time,))  # Execute the query
            result = query_response.fetchall()  # Get all the results from the query
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the list of humidity if match, otherwise 'No database entry found!'
        return result if len(result) > 0 else 'No database entry found!'

    def get_time_reading_at_humidity(self, humidity):
        """
        This function is used to get the time at the given humidity. 
        :param humidity: int, humidity

        :return: list of humidity if match, otherwise 'No database entry found!'
        """
        sqlite_table_where_query = """ SELECT Timestamp
                                       FROM humidity
                                       WHERE Humidity = ?"""

        try:
            query_response = self.cursor.execute(
                sqlite_table_where_query, (humidity,))
            result = query_response.fetchall()
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the list of humidity if match, otherwise 'No database entry found!'
        return result if len(result) > 0 else 'No database entry found!'
