# import necessary libraries
import openai
from dotenv import dotenv_values
from speech_to_text import SpeechToText
from chat_completion import ChatCompletion

# example from ajit database
currentTemperature = "24"
currentHumidity = "70"

# load API key from the .env file
config = dotenv_values(".env")

# set the OpenAI API key using the loaded value
openai.api_key = config["OPENAI_API_KEY"]

# create a SpeechToText instance
speech_to_text = SpeechToText(openai, config["SPEECH_TO_TEXT_MODEL"])

# transcribe audio to text
text = speech_to_text.transcribe("assets/audio/capitality_of_indonesia.wav")

# create a ChatCompletion instance
chat_completion = ChatCompletion(openai, config["CHAT_COMPLETION_MODEL"])

# obtain an answer using the ChatCompletion instance
answer = chat_completion.get_answer(text, [
    "statement 1: my location is my room" # change this my room to location data where the senseHAT is located
    "statement 2: current humidity in my location is" + currentHumidity + "percent" # change this 70 to humidity data from data base
    "statement 3: current temperature in my location is"+ currentTemperature +"degrees celcius" # change this 24 to temperature data from data base
    "Keep every answer short and concise." # make the answer short and conscise
])

# print the question and answer
print(f"Question: {text}")
print(f"Answer: {answer}")
