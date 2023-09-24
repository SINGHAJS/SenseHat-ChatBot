# import necessary libraries
import openai
from dotenv import dotenv_values
from chat_completion import ChatCompletion

# example data from Ajit's database
current_temperature = 24
current_humidity = 70

# load API key from the .env file
config = dotenv_values(".env")

# set the OpenAI API key using the loaded value
openai.api_key = config["OPENAI_API_KEY"]

# create a ChatCompletion instance
chat_completion = ChatCompletion(openai, config["CHAT_COMPLETION_MODEL"])

# import the SpeechToText class
from speech_to_text import SpeechToText

# define the path to the Google Cloud Speech Recognition credentials
credentials_path = "assets/sa_speech_recognition.json"

# create a SpeechToText instance with the specified credentials
speech_to_text = SpeechToText(credentials_path=credentials_path)

# specify the path to the audio file to be transcribed
audio_file = "assets/audio/capitality_of_indonesia.wav"

# transcribe the audio file and store the result
result = speech_to_text.transcribe(file_path=audio_file)

# print the transcribed text
print(f"Prompt: {result}")

# define keywords related to temperature and humidity
keywords_temperature = [
    "temperature",
    "room",
]

keywords_humidity = [
    "humidity",
    "room",
]

# define a function to check if input text contains specified keywords
def has_keywords(input_text, keywords):
    input_text = input_text.lower()
    splitted = input_text.split(" ")

    for word in splitted:
        if word in keywords:
            keywords.remove(word)
    
    return (len(keywords) == 0)

answer = None
# check if the transcribed text contains keywords related to temperature or humidity
if has_keywords(result, keywords_temperature):
    print(f"Answer: Current temperature in the room is {current_temperature}")
elif has_keywords(result, keywords_humidity):
    print(f"Answer: Current humidity in the room is {current_humidity}")
else:
    # obtain an answer using the ChatCompletion instance
    answer = chat_completion.get_answer(result,[
        "Keep every answer short and concise." # make the answer short and concise
    ])

    # print the generated answer
    print(f"Answer: {answer}")
