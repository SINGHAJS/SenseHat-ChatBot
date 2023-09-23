# class for chat-based completion
class ChatCompletion:
    def __init__(self, openai, model: str = "gpt-3.5-turbo"):
        self.__model = model
        self.__openai = openai

    # method to obtain an answer based on a question and premises
    def get_answer(self, question: str, premises: list, randomness=0):
        
        # Create messages with system and user roles
        messages = [{"role": "system", "content": p} for p in premises]
        messages.append({"role": "user", "content": question})
        
        # Generate a response using the specified model and messages
        response = self.__openai.ChatCompletion.create(
            model=self.__model,
            messages=messages,
            temperature=randomness,
        )

        # Extract and return the content of the response
        return response["choices"][0]["message"]["content"]
