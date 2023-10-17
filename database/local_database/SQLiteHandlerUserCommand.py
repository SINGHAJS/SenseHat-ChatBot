import SQLiteDatabaseHandler
import sqlite3 as SQLite


class SQLiteHandlerUserCommand(SQLiteDatabaseHandler):

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
