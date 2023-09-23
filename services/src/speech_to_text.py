# Import necessary libraries
import openai          # Import the OpenAI library for API access
from dotenv import dotenv_values   # Import the dotenv library for loading environment variables

# Load API key from the .env file
config = dotenv_values(".env")   # Load environment variables from the .env file

# Set the OpenAI API key using the loaded value
openai.api_key = config["OPENAI_API_KEY"]

# Open the audio file for transcription in binary read mode
with open("assets/audio/HumidityCurrent.wav", "rb") as f:
    # Transcribe the audio using the OpenAI GPT-3.5 Whisper model
    transcript = openai.Audio.transcribe("whisper-1", f)

    # Print the transcription result
    print(transcript)
