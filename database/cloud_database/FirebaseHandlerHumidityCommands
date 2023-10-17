import FirebaseHandler
from datetime import datetime


class FirebaseHandlerHumidityCommands(FirebaseHandler):
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
