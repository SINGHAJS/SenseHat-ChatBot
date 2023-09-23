# import necessary libraries
import openai
from dotenv import dotenv_values

# load API key from the .env file
config = dotenv_values(".env")

# define a ChatCompletion class for handling OpenAI Chat models
class ChatCompletion:
    def __init__(self, openai_api_key: str, model: str = "gpt-3.5-turbo"):
        self.openai_api_key = openai_api_key
        self.__model = model
        openai.api_key = openai_api_key

    # method for obtaining a chat-based response from the OpenAI model
    def get_answer(self):
        response = openai.ChatCompletion.create(
            model=self.__model,
            messages=[
                {"role": "system", "content": "Hi, what is the humidity now?"}
            ],
            temperature=0
        )

        print(response)

# create an instance of the ChatCompletion class with the API key from the .env file
chat_completion = ChatCompletion(config["OPENAI_API_KEY"])

# call the get_answer method to get a response from the OpenAI model
chat_completion.get_answer()
