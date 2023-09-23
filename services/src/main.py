# import necessary libraries
import openai
from dotenv import dotenv_values
from speech_to_text import SpeechToText
from chat_completion import ChatCompletion

# load API key from the .env file
config = dotenv_values(".env")

# set the OpenAI API key using the loaded value
openai.api_key = config["OPENAI_API_KEY"]

# create a SpeechToText instance
speech_to_text = SpeechToText(openai, config["SPEECH_TO_TEXT_MODEL"])

# transcribe audio to text
text = speech_to_text.transcribe("assets/audio/HumidityNow.wav")

# create a ChatCompletion instance
chat_completion = ChatCompletion(openai, config["CHAT_COMPLETION_MODEL"])

# obtain an answer using the ChatCompletion instance
answer = chat_completion.get_answer(text, [
    "here is a class"
    "current humidity in here is 70 percent"
    "current temperature in here is 24"
])

# print the question and answer
print(f"Question: {text}")
print(f"Answer: {answer}")
