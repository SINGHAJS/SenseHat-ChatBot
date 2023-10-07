#environmental-sensors.py 
import os
import argparse
from datetime import datetime
from sense_hat import SenseHat
import logging

# Constants
FOLDER_PATH = "/home/s13/projects/sensehat_chatbot/embedded/assets/"
VALID_MEASUREMENTS = ['temp', 'humi']

# Configure logging
logging.basicConfig(level=logging.INFO)


class SenseHatMeasurement:

    def __init__(self):
        self.sense_hat = SenseHat()

    def get_temperature(self):
        """Returns temperature from the Sense Hat."""
        return self.sense_hat.get_temperature()

    def get_humidity(self):
        """Returns humidity from the Sense Hat."""
        return self.sense_hat.get_humidity()

    def get_measurement(self, measurement_type):
        """Returns the desired measurement based on the provided type."""
        if measurement_type == "temp":
            return self.get_temperature()
        elif measurement_type == "humi":
            return self.get_humidity()
        else:
            raise ValueError("Invalid measurement type provided.")

    def write_to_file(self, timestamp, value, measurement_type):
        """Writes timestamp and measurement value to a file."""
        folder_map = {
            'temp': 'temperature_data',
            'humi': 'humidity_data'
        }
        folder_name = os.path.join(FOLDER_PATH, folder_map[measurement_type])
        file_name = f"{folder_map[measurement_type]}.txt"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        with open(os.path.join(folder_name, file_name), "a") as file:
            file.write(f"{timestamp}, {value}\n")

        logging.info(f"Data written to file: {timestamp}, {value}")


def main(args):
    """Main Function to get measurement and write to file."""
    sh_measurement = SenseHatMeasurement()
    measurement_type = args.measurement_type
    value = sh_measurement.get_measurement(measurement_type)

    if value is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sh_measurement.write_to_file(timestamp, value, measurement_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get temperature or humidity from Sense Hat.")
    parser.add_argument("measurement_type", choices=VALID_MEASUREMENTS, help="Type of measurement (temp/humi).")
    args = parser.parse_args()
    main(args)
