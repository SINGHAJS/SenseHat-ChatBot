import os
import openai
from dotenv import dotenv_values
from chat_completion import ChatCompletion
from speech_to_text import SpeechToText

# CONSTANTS
AUDIO_DIRECTORY = "../../embedded/assets/audio_files/current_user_prompt"
CREDENTIALS_PATH = "../../credentials/chatbotproject-401307-d4e1b394c4f5.json"
CURRENT_TEMPERATURE = 24
CURRENT_HUMIDITY = 70
KEYWORDS_TEMPERATURE = ["temperature", "room"]
KEYWORDS_HUMIDITY = ["humidity", "room"]

# Configuration
config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")

def get_audio_file(directory):
    """Retrieve the first WAV file from a directory."""
    wav_files = [f for f in os.listdir(directory) if f.endswith(".wav")]

    if not wav_files:
        print("No .wav files found in the 'audio' directory.")
        return None

    return os.path.join(directory, wav_files[0])

def has_keywords(input_text, keywords):
    """Check if input text contains all specified keywords."""
    input_text = input_text.lower().split()

    return all(word in input_text for word in keywords)

def main():
    # Initialization
    chat_completion = ChatCompletion(openai, "gpt-3.5-turbo")
    speech_to_text = SpeechToText(credentials_path=CREDENTIALS_PATH)
    audio_file = get_audio_file(AUDIO_DIRECTORY)

    if not audio_file:
        return

    # Transcription
    result = speech_to_text.transcribe(file_path=audio_file)
    print(f"Prompt: {result}")

    # Keyword Matching
    if has_keywords(result, KEYWORDS_TEMPERATURE):
        print(f"Answer: Current temperature in the room is {CURRENT_TEMPERATURE}")
    elif has_keywords(result, KEYWORDS_HUMIDITY):
        print(f"Answer: Current humidity in the room is {CURRENT_HUMIDITY}")
    else:
        # Chat completion
        answer = chat_completion.get_answer(result, [
            "Keep every answer short and concise." # Guideline for the model
        ])
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
