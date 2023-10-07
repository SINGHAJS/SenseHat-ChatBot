import os
import openai
from dotenv import load_dotenv
from chat_completion import ChatCompletion
from speech_to_text import SpeechToText

class ChatbotAssistant:
    AUDIO_DIRECTORY = "../../embedded/assets/audio_files/current_user_prompt"
    CREDENTIALS_PATH = "../../credentials/chatbotproject-401307-d4e1b394c4f5.json"
    CURRENT_TEMPERATURE = 24
    CURRENT_HUMIDITY = 70
    KEYWORDS_TEMPERATURE = ["temperature", "room"]
    KEYWORDS_HUMIDITY = ["humidity", "room"]

    def __init__(self):
        # Load API keys and configurations
        load_dotenv()
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self.chat_completion = ChatCompletion(openai, "gpt-3.5-turbo")
        self.speech_to_text = SpeechToText(credentials_path=self.CREDENTIALS_PATH)

    def _get_audio_file(self):
        """Retrieve the first WAV file from a directory."""
        try:
            wav_files = [f for f in os.listdir(self.AUDIO_DIRECTORY) if f.endswith(".wav")]

            if not wav_files:
                print("No .wav files found in the 'audio' directory.")
                return None

            return os.path.join(self.AUDIO_DIRECTORY, wav_files[0])
        except Exception as e:
            print(f"Error accessing audio directory: {e}")
            return None

    def _has_keywords(self, input_text, keywords):
        """Check if input text contains all specified keywords."""
        input_text = input_text.lower().split()
        return all(word in input_text for word in keywords)

    def run(self):
        audio_file = self._get_audio_file()

        if not audio_file:
            return

        try:
            result = self.speech_to_text.transcribe(file_path=audio_file)
            if not result:
                print("There is no speech in the audio file.")
                return

            print(f"Prompt: {result}")
        except Exception as e:
            print(f"Error during transcription: {e}")
            return

        if self._has_keywords(result, self.KEYWORDS_TEMPERATURE):
            print(f"Answer: Current temperature in the room is {self.CURRENT_TEMPERATURE}")
        elif self._has_keywords(result, self.KEYWORDS_HUMIDITY):
            print(f"Answer: Current humidity in the room is {self.CURRENT_HUMIDITY}")
        else:
            try:
                answer = self.chat_completion.get_answer(result, [
                    "Keep every answer short and concise."
                ])
                print(f"Answer: {answer}")
            except Exception as e:
                print(f"Error obtaining chat completion: {e}")

if __name__ == "__main__":
    assistant = ChatbotAssistant()
    assistant.run()
