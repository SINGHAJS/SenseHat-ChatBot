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
    firebase_handler.save_temperatre(temperature_value)
    firbase_handler.get_all_temperature_values()
    firebase_handler.get_single_temperature_value_at_time()
    firebase_handler.get_multi_temperature_value_at_time()
    firebase_handler.get_single_time_value_at_temperature()
    firebase_handler.get_multi_time_value_at_temperature()

    # Humidity
    firebase_handler.save_humidity(humidity_value)
    firbase_handler.get_all_humidity_values()
    firebase_handler.get_single_humidity_value_at_time()
    firebase_handler.get_multi_humidity_value_at_time()
    firebase_handler.get_single_time_value_at_humidity()
    firebase_handler.get_multi_time_value_at_humidity()
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

    # This function is used to save temperature to the Firebase database
    def save_temperature(self, temperature):
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format timestamp

        # Push the temperature and the timestamp to the Firebase database
        self.db_temperature_ref.push().set(
            {'temperature-value': temperature, "timestamp": formatted_timestamp})

    # This function is used to get and return all the temperature values from the Firebase database
    def get_all_temperature_values(self):
        # Returns a dictionary of the temperature values
        return self.db_temperature_ref.get()

    # This function is used to get and return a single temperature value at the given timestamp
    def get_single_temperature_value_at_time(self, time):
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()

        for key, value in all_temperatre_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Return the temperature value if there is a match
                return value['temperature-value']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    # This function is used to get and return multiple temperature values at the given timestamp
    def get_multi_temperature_values_at_time(self, time):
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

    # This function is used to get and return single timestamp value at the given temperature
    def get_single_time_value_at_temperature(self, temperature):
        # Gets all the temperature values
        all_temperatre_values = self.get_all_temperature_values()

        for key, value in all_temperatre_values.items():
            # Check if the temperature value in the Firebase database matches the given temperature
            if (value['temperature-value'] == temperature):
                # Return the timestamp value if there is a match
                return value['timestamp']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    # This function is used to get and return multiple timestamp values at the given temperature
    def get_multi_time_values_at_temperature(self, temperature):
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

    # This function is used to save humidity to the Firebase database
    def save_humidity(self, humidity):
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format the timestamp

        # Push the humidity and the timestamp to the Firebase database
        self.db_humidity_ref.push().set(
            {'humidity-value': humidity, "timestamp": formatted_timestamp})

   # This function is used to get and return all the humidity values from the Firebase database
    def get_all_humidity_values(self):
        # Returns a dictionary of the humidity values
        return self.db_humidity_ref.get()

    # This function is used to get and return a single humidty value at the given timestamp
    def get_single_humidity_value_at_time(self, time):
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values

        for key, value in all_humidity_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Return the humidity value if there is a match
                return value['humidity-value']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    # This function is used to get and return multiple humidity values at the given timestamp
    def get_multi_humidity_values_at_time(self, time):
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values
        humidity_values = []  # Initialise the humidity list

        for key, value in all_humidity_values.items():
            # Check if the timestamp in the Firebase database matches the given timestamp
            if (value['timestamp'] == time):
                # Append the humidity value to the list if there is a match
                humidity_values.append(value['humidity-value'])

        # Returns the list of humidity values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return humidity_values if len(humidity_values) > 0 else 'No database entry found!'

    # This function is used to get and return single timestamp value at the given humidity
    def get_single_time_value_at_humidity(self, humidity):
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values

        for key, value in all_humidity_values.items():
            # Check if the humidity value in the Firebase database matches the given humidity
            if (value['humidity-value'] == humidity):
                # Return the timestamp value if there is a match
                return value['timestamp']

        # Return 'No database entry found!' when no match is found
        return 'No database entry found!'

    # This function is used to get and return multiple timestamp values at the given humidity
    def get_multi_time_values_at_humidity(self, humidity):
        all_humidity_values = self.get_all_humidity_values()  # Gets all the humidity values
        humidity_time_values = []  # Initialise the humidity timestamp list

        for key, value in all_humidity_values.items():
            # Check if the humidity value in the Firebase database matches the given humidity
            if (value['humidity-value'] == humidity):
                # Append the timestamp value to the list if there is a match
                humidity_time_values.append(value['timestamp'])

        # Returns the list of timestamp values if the length of the list is greater than 0, otherwise it returns 'No database entry found!'
        return humidity_time_values if len(humidity_time_values) > 0 else 'No database entry found!'
