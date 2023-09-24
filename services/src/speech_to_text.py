# import necessary libraries
import openai          # import the OpenAI library for API access
from dotenv import dotenv_values   # import the dotenv library for loading environment variables

# load API key from the .env file
config = dotenv_values(".env")   # load environment variables from the .env file

# set the OpenAI API key using the loaded value
openai.api_key = config["OPENAI_API_KEY"]

# open the audio file for transcription in binary read mode
with open("assets/audio/HumidityCurrent.wav", "rb") as f:
    # transcribe the audio using the OpenAI GPT-3.5 Whisper model
    transcript = openai.Audio.transcribe("whisper-1", f)

    # print the transcription result
    print(transcript)
