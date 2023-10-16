import FirebaseHandler
from datetime import datetime


class FirebaseHandlerTemperatureCommands(FirebaseHandler):
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
