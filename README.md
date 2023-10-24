# SenseHat ChatBot
The SenseHat ChatBot is a system that poses as a device to assist the user answer questions related to reading environmental data (temperature, humidity) and answering general knowledge questions. Additionally, it stores sensory, user prompt, and chatbot response data locally using SQLite that is then pushed to the Firebase database with a scheduler called Crontab. 

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

1. **Temperature Sensor Data:** The ChatBot is able to provide the temperaute sensor data when prompted. 

2. **Humidity Sensor Data:** The ChatBot is able to provide the humidity sensor data when prompted by the user. 

3. **Humidity Sensor Data:** The ChatBot is able to answer general knowledge questions using OpenAI. 

4. **Data Storage:** The ChatBot stores data locally and remotely. 

## Technologies Used

- Raspberry Pi 4
- SenseHat (Temperature Sensor, Humidity Sensor, 64 Pixel Display, Toggle Stick)
- Python
- Google Voice-to-Text
- OpenAI 
- SQLite 
- Firebase
- Crontab

## Installation

1. On RPi 4 with SenseHat, Clone the repository: `git clone https://github.com/SINGHAJS/SenseHat-ChatBot.git`
2. Open the project directory on the RPi 4.
3. Open terminal in the project directory and enter `pip install -r requirements.txt`
4. If on mac, activate virtual environment using the command `source venv/bin/activate`
5. Once the virtual environment activates, enter `cd services/src`
6. Execute the program using the command `python3 main.py`

## Usage

Upon following the installation processess:

1. **Record User Prompt:** Press the toggle stick and prompt the ChatBot with a question. The 64 Pixels should show a red recording symbol. 

2. **ChatBot Response:** Once the prompt is recorded, the ChatBot should display the response on the 64 Pixels display.
