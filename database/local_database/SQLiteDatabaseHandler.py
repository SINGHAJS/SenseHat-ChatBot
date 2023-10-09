import sqlite3 as SQLite


class SQLiteDatabaseHandler:
    connection = None
    cursor = None

    def __init__(self, db_reference="chatbot-memory.db"):
        self.db_reference = db_reference

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

    def create_user_table(self):
        """
        This function is used to create user table if it does not exist.
        """
        sqlite_table_creation_query = """CREATE TABLE IF NOT EXISTS user ( 
            Id INTEGER PRIMARY KEY, 
            UserInput TEXT NOT NULL, 
            ChatBotResponse TEXT NOT NULL,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""  # User table creation query

        try:
            # Execute the table creation query
            self.cursor.execute(sqlite_table_creation_query)
            self.connection.commit()  # Commmit changes to the database
            print("[ USER TABLE CREATED ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def insert_into_user_table(self, user_input, chatbot_response):
        """
        This function is used to insert a new user reading into the user table.
        :param user_input: str, user_input
        :param chatbot_response: str, chatbot_response

        """
        # User table insertion query
        sqlite_table_insertion_query = f""" INSERT INTO user (UserInput, ChatBotResponse) VALUES (?, ?) """

        try:
            # Execute table insertion query
            self.cursor.execute(sqlite_table_insertion_query,
                                (user_input.upper(), chatbot_response.upper()))
            self.connection.commit()  # Commit changes to the database
            print(
                f"[ INSERTED {user_input} and {chatbot_response} INTO USER TABLE ]")
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

    def get_user_interaction_data(self):
        """
        This function is used to get the user readings from the user table in the database.
        Once the results are retrieved, the functions returns the results.

        :return: list of user readings
        """
        sqlite_table_get_query = """SELECT * FROM user"""  # User values retrieval query

        try:
            # Execute table retreival query
            self.cursor.execute(sqlite_table_get_query)
            query_response = self.cursor.fetchall()  # Fetch all the results
            print(query_response)
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the user results
        return query_response if len(query_response) > 0 else 'No data entry avaliable!'

    def get_chatbot_response_from_user_input(self, user_input):
        """
        This function is used to get the chatbot response store based on user inputs. 
        :param user_input: str, user_input

        :return: list of user inputs if match, otherwise 'No database entry found!'
        """
        sqlite_table_where_query = """ SELECT ChatbotResponse
                                       FROM user
                                       WHERE UserInput = ?"""

        try:
            query_response = self.cursor.execute(
                sqlite_table_where_query, (user_input.upper(),))
            result = query_response.fetchall()
        except SQLite.Error as e:
            print(f"[DATABASE ERROR: {e}]")
            self.terminate_db_connection()  # Terminate connections

        # Return the list of user inputs if match, otherwise 'No database entry found!'
        return result if len(result) > 0 else 'No database entry found!'

    def terminate_db_connection(self):
        """
        This function terminates the database and cursor connection
        """
        print("[ CLOSING DATABASE CONNECTIONS ]")
        self.cursor.close()
        self.connection.close()
        print("[ SUCCESSFULLY CLOSED DATABASE CONNECTIONS ]")
