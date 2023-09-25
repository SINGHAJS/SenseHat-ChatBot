import os
from datetime import datetime
from sense_hat import SenseHat
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize SenseHat
sense = SenseHat()

def get_temperature():
    """
    Get Temperature from Sense Hat.
    :return: float, temperature in degrees Celsius
    """
    try:
        temperature = sense.get_temperature()
        logging.info(f"Temperature: {temperature}")
        return temperature
    except Exception as e:
        logging.error(f"Error getting temperature: {e}")
        return None

def write_to_file(timestamp, temperature, folder_name="../assets/temperature_data", file_name="temperature_data.txt"):
    """
    Write timestamp and temperature to file.
    :param timestamp: str, timestamp
    :param temperature: float, temperature
    :param folder_name: str, folder to store the data
    :param file_name: str, file to store the data
    """
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        with open(os.path.join(folder_name, file_name), "a") as file:
            file.write(f"{timestamp}, {temperature}\n")
        logging.info(f"Data written to file: {timestamp}, {temperature}")
    except Exception as e:
        logging.error(f"Error writing to file: {e}")

def main():
    """
    Main Function to get temperature and write to file.
    """
    temperature = get_temperature()
    if temperature is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_to_file(timestamp, temperature)

if __name__ == "__main__":
    main()
