import os
import openai
from dotenv import load_dotenv
from chat_completion import ChatCompletion
from speech_to_text import SpeechToText
from ...database.local_database.SQLiteDatabaseHandler import SQLiteDatabaseHandler


class ChatBot:
    
    def __init__(self):
        self.audio_directory = "../../embedded/assets/audio_files/current_user_prompt"
        self.wav_files = [f for f in os.listdir(self.audio_directory) if f.endswith(".wav")]
        self.current_temperature = 24
        self.current_humidity = 70
        self.db = SQLiteDatabaseHandler()
        self.db.establish_db_connection()
        self.db.create_user_table()
        load_dotenv()
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self.chat_completion = ChatCompletion(openai, "gpt-3.5-turbo")
        self.credentials_path = "../../credentials/chatbotproject-401307-d4e1b394c4f5.json"
        self.speech_to_text = SpeechToText(credentials_path=self.credentials_path)
        self.responses_file = "/home/s13/projects/sensehat_chatbot/embedded/assets/responses/responses.txt"

    def write_response_to_file(self, response_text):
        with open(self.responses_file, 'w') as file:
            file.write(response_text)

    def has_keywords(self, input_text, keywords):
        input_text = input_text.lower()
        splitted = input_text.split(" ")
        for word in splitted:
            if word in keywords:
                keywords.remove(word)
        return (len(keywords) == 0)

    def run(self):
        if not self.wav_files:
            print("No .wav files found in the 'audio' directory.")
            return

        audio_file = os.path.join(self.audio_directory, self.wav_files[0])
        result = self.speech_to_text.transcribe(file_path=audio_file)
        
        if not result:
            print("No speech detected in the audio file.")
            return

        print(f"Prompt: {result}")

        keywords_temperature = ["temperature", "room"]
        keywords_humidity = ["humidity", "room"]

        answer = None
        if self.has_keywords(result, keywords_temperature[:]):
            answer = f"Current temperature in the room is {self.current_temperature}"

        elif self.has_keywords(result, keywords_humidity[:]):
            answer = f"Current humidity in the room is {self.current_humidity}"
        else:
            answer = self.chat_completion.get_answer(result, ["make the answers atleast 5 words."])

        print(f"Answer: {answer}")
        self.db.insert_into_user_table(result, answer)
        self.write_response_to_file(answer)
        

        
        
        # keyword -> 2 
                        # string cuurent temp in room is + self.current_temp" (string ,string)
        # keywords < 2
                        # open ai to get reponse
        


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
