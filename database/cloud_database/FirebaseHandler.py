import firebase_admin as FireMan
from firebase_admin import db, credentials
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

        self.db_local_temperature_data_ref = self.db_root_ref.child(
            'local-temperature-data/')  # Reference to the local temperature data

        self.db_local_humidity_data_ref = self.db_root_ref.child(
            'local-humidity-data/')  # Reference to the local humidity data

        self.db_local_user_interactions_data_ref = self.db_root_ref.child(
            'local-user-interaction-data/')  # Reference to the local user interaction data

    def push_local_temprature_date_to_cloud(self, temperature_data_list):
        """
        This function takes a list of temperature data and pushes this this list of data into the cloud database. It 
        is intended to be used for push the local database data into the cloud. 
        :param temperature_data_list: list of temperature data
        """

        data_list = []

        for item in temperature_data_list:
            temperature = item[1]
            timestamp = item[2]

            data_list.append(
                {'temperature-value': temperature, 'timestamp': timestamp})

        self.db_local_temperature_data_ref.push().set(data_list)

    def push_local_humidity_date_to_cloud(self, humidity_data_list):
        """
        This function takes a list of humidity data and pushes this this list of data into the cloud database. It 
        is intended to be used for push the local database data into the cloud. 
        :param humidity_data_list: list of humidity data
        """

        data_list = []

        for item in humidity_data_list:
            humidity = item[1]
            timestamp = item[2]

            data_list.append(
                {'humidity-value': humidity, 'timestamp': timestamp})

        self.db_local_humidity_data_ref.push().set(data_list)

    def push_local_user_interactions_date_to_cloud(self, user_interactions_data):
        """
        This function takes a list of user interaction data and pushes this this list of data into the cloud database. It 
        is intended to be used for push the local database data into the cloud. 
        :param user_interactions_data: list of user interaction data
        """

        data_list = []

        for item in user_interactions_data:
            user_prompt = item[1]
            chatbot_response = item[2]
            timestamp = item[3]

            data_list.append(
                {'user_prompt': user_prompt, 'chatbot_response': chatbot_response, 'timestamp': timestamp})

        self.db_local_user_interactions_data_ref.push().set(data_list)
