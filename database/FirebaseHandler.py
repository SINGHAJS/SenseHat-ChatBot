"""
@Ussage Guide
#1 Import and create an instance of the FirebaseHandler class

@explanation
    The code below creates an instance of the FirebaseHandler class. This will 
    be used to use the functions provided by the FirebaseHandler class.

<code> 
    from database.FirebaseHandler import FirebaseHandler
    firebase_handler = FirebaseHandler() # Creating an instace of the FirebaseHandler
</code>

#2 Now you can use the functions offered by the FirebaseHandler class

@explanation
    Below is a list of functions offered by the FirebaseHandler class.

<code> 
    # Temperature
    firebase_handler.save_temperatre(temperature_value: int)
    firbase_handler.get_all_temperature_values() : dictionary
    firebase_handler.get_single_temperature_value_at_time() : int
    firebase_handler.get_multi_temperature_value_at_time() : list
    firebase_handler.get_single_time_value_at_temperature() : str
    firebase_handler.get_multi_time_value_at_temperature() : list

    # Humidity
    firebase_handler.save_humidity(humidity_value: int)
    firbase_handler.get_all_humidity_values() : dictionary
    firebase_handler.get_single_humidity_value_at_time() : int
    firebase_handler.get_multi_humidity_value_at_time() : list
    firebase_handler.get_single_time_value_at_humidity() : str
    firebase_handler.get_multi_time_value_at_humidity() : list

    #User 
    firebase_handler.save_user_interaction(user_input: str, chatbot_response: str)
    firebase_handler.get_all_user_interactions(): list
    firebase_handler.get_single_chatbot_response_from_user_input(user_input: str) : list
    firebase_handler.get_multi_chatbot_response_from_user_input(user_input: str) : list
</code>

@Troubleshooting
    If an error is encountered, please ensure the firebase_admin package is installed. 
    Also, ensure that the FirebasHandler class is being imported correctly.
"""

import firebase_admin as FireMan
from firebase_admin import db, credentials
import time
from datetime import datetime
import os


class FirebaseHandler:
    database_url = 'https://ense810-emb-chatbot-default-rtdb.firebaseio.com/'

    def __init__(self):
        # Get the path of the private key file based on the current working file
        firebase_private_key_path = os.path.join(
            os.path.pardir, 'credentials', 'FirebasePrivateKey.json')

        # Creates a credentials object to authenticate with Firebase
        creds = credentials.Certificate(
            firebase_private_key_path)

        # Initialises the app with the Firebase credentials
        firebase_app = FireMan.initialize_app(creds, {
            'databaseURL': self.database_url})

        # Firebase database references
        self.db_root_ref = db.reference('chatbot-memory/', app=firebase_app)
        self.db_temperature_ref = self.db_root_ref.child(
            'temperature/')  # Reference to the temperature

        self.db_humidity_ref = self.db_root_ref.child(
            'humidity/')  # Reference to the humidity

        self.db_user_ref = self.db_root_ref.child(
            'user-interaction/')  # Reference to the user interaction

    def save_temperature(self, temperature):
        """
        This function is used to save temperature to the Firebase database
        :param temperature: int, temperature
        """
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format timestamp

        # Push the temperature and the timestamp to the Firebase database
        self.db_temperature_ref.push().set(
            {'temperature-value': temperature, "timestamp": formatted_timestamp})

    def get_all_temperature_values(self):
        """
        This function is used to get and return all the temperature values from the Firebase database
        :return: dictionary temperature values 
        """
        return self.db_temperature_ref.get()

    def get_single_temperature_value_at_time(self, time):
        """
        This function is used to get and return a single temperature value at the given timestamp
        :param time: str, time

        :return: int, temperature value if match, otherwise 'No database entry found!'
        """
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()

        for key, value in all_temperatre_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Return the temperature value if there is a match
                return value['temperature-value']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    def get_multi_temperature_values_at_time(self, time):
        """
        This function is used to get and return multiple temperature values at the given timestamp
        :param time: str, time

        :return: list of temperature values if len(list) > 0, otherwise 'No database entry found!'
        """
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()
        temperature_values = []  # Initialise temperature list

        for key, value in all_temperatre_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Append the temperature value to the list if there is a match
                temperature_values.append(value['temperature-value'])

        # Returns the list of temperature values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return temperature_values if len(temperature_values) > 0 else 'No database entry found!'

    def get_single_time_value_at_temperature(self, temperature):
        """
        This function is used to get and return single timestamp value at the given temperature
        :param temperature: temperature, int

        :return: str, timestamp if found, otherwise 'No database entry found!'
        """
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()

        for key, value in all_temperatre_values.items():
            # Check if the temperature value in the Firebase database matches the given temperature
            if (value['temperature-value'] == temperature):
                # Return the timestamp value if there is a match
                return value['timestamp']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    def get_multi_time_values_at_temperature(self, temperature):
        """
        This function is used to get and return multiple timestamp values at the given temperature
        :param temperature: int, tempearture

        :return: list of timestamps if len(list) > 0, otherwise 'No database entry found!'
        """
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()
        temperature_time_values = []  # Initialise temperature time list

        for key, value in all_temperatre_values.items():
            # Check if the temperature value in the Firebase database matches the given temperature
            if (value['temperature-value'] == temperature):
                # Append the timestamp value to the list if there is a match
                temperature_time_values.append(value['timestamp'])

        # Returns the list of timestamp values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return temperature_time_values if len(temperature_time_values) > 0 else 'No database entry found!'

    def save_humidity(self, humidity):
        """
        This function is used to save humidity to the Firebase database
        :param humidity: int, humidity
        """
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format the timestamp

        # Push the humidity and the timestamp to the Firebase database
        self.db_humidity_ref.push().set(
            {'humidity-value': humidity, "timestamp": formatted_timestamp})

    def get_all_humidity_values(self):
        """
        This function is used to get and return all the humidity values from the Firebase database        
        :return: dictionary humidity values 
        """
        return self.db_humidity_ref.get()

    def get_single_humidity_value_at_time(self, time):
        """
        This function is used to get and return a single humidty value at the given timestamp        
        :param time: str, time

        :return: int, humidity value if match, otherwise 'No database entry found!'
        """
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values

        for key, value in all_humidity_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Return the humidity value if there is a match
                return value['humidity-value']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    def get_multi_humidity_values_at_time(self, time):
        """
        This function is used to get and return multiple humidity values at the given timestamp
        :param time: str, time

        :return: list of humidity values if len(list) > 0, otherwise 'No database entry found!'
        """
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values
        humidity_values = []  # Initialise the humidity list

        for key, value in all_humidity_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Append the humidity value to the list if there is a match
                humidity_values.append(value['humidity-value'])

        # Returns the list of humidity values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return humidity_values if len(humidity_values) > 0 else 'No database entry found!'

    def get_single_time_value_at_humidity(self, humidity):
        """
        This function is used to get and return single timestamp value at the given humidity        
        :param humidity: humidity, int

        :return: str, timestamp if found, otherwise 'No database entry found!'
        """
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values

        for key, value in all_humidity_values.items():
            # Check if the humidity value in the Firebase database matches the given humidity
            if (value['humidity-value'] == humidity):
                # Return the timestamp value if there is a match
                return value['timestamp']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    def get_multi_time_values_at_humidity(self, humidity):
        """
        This function is used to get and return multiple timestamp values at the given humidity        
        :param humidity: int, humidity

        :return: list of timestamps if len(list) > 0, otherwise 'No database entry found!'
        """
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values
        humidity_time_values = []  # Initialise the humidity timestamp list

        for key, value in all_humidity_values.items():
            # Check if the humidity value in the Firebase database matches the given humidity
            if (value['humidity-value'] == humidity):
                # Append the timestamp value to the list if there is a match
                humidity_time_values.append(value['timestamp'])

        # Returns the list of timestamp values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return humidity_time_values if len(humidity_time_values) > 0 else 'No database entry found!'

    def save_user_interaction(self, user_input, chatbot_response):
        """
        This function is used to save the user inputs and the responses it gets from the chatbot. 
        :param user_input: str, user_input
        :param chatbot_response: str, chatbot_response
        """
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format the timestamp

        # Push the user input, chatbot response, and the timestamp to the Firebase database
        self.db_user_ref.push().set(
            {'user-input': user_input.upper(), 'chatbot-response': chatbot_response.upper(), "timestamp": formatted_timestamp})

    def get_all_user_interactions(self):
        """
        This function is used to get all the user interactions with the chatbot. 
        :return: dictionary of user interactions
        """
        return self.db_user_ref.get()

    def get_single_chatbot_response_from_user_input(self, user_input):
        """
        This function is used to get the chatbot response based on the user input. 
        :param user_input: str, user_input

        :return: list of chatbot response if match if found, otherwise 'No databse entry found!'
        """
        all_user_interactions = self.get_all_user_interactions()  # Get all the user interactions

        for key, value in all_user_interactions.items():
            # Check if there is a match for the user input
            if (value['user-input'] == user_input.upper()):
                # Return the chatbot response if a match is found
                return value['chatbot-response']

        # Return 'No databse entry found!' if no match found
        return 'No database entry found!'

    def get_multi_chatbot_response_from_user_input(self, user_input):
        """
        This function is used to get multiple chatbot response to the same user input if any. 
        :param user_input: str, user_input

        :return: list of chatbot responses
        """
        # Get all the user interactions
        all_user_interactions = self.get_all_user_interactions()
        chatbot_response_list = []  # Initialse chatbot response list

        for key, value in all_user_interactions.items():
            # Check if there is a match for the user input
            if (value['user-input'] == user_input.upper()):
                # Append the chatbot response to the list if a match is found
                chatbot_response_list.append(value['chatbot-response'])

        # Return the chatbot response if the list size if greater than 0, otherwise, return 'No database entry found!'
        return chatbot_response_list if len(chatbot_response_list) > 0 else 'No database entry found!'
