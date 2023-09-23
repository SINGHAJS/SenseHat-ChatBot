import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

class ChatCompletion:
    def __init__(self, openai_api_key: str, model: str = "gpt-3.5-turbo"):
        self.openai_api_key = openai_api_key
        self.__model = model
        openai.api_key = openai_api_key

    def get_answer(self):
        response = openai.ChatCompletion.create(
            model= self.__model,
            messages=[
                {"role": "system", "content": "Hi, what is the humidity now?"}
            ],
            temperature=0
        )

        print(response)

chat_completion = ChatCompletion(config["OPENAI_API_KEY"])

chat_completion.get_answer()




