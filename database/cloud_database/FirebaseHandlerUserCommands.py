import FirebaseHandler
from datetime import datetime


class FirebaseHandlerUserCommands(FirebaseHandler):
    def save_user_interaction(self, user_input, chatbot_response):
        """
        This function is used to save the user inputs and the responses it gets from the chatbot. 
        :param user_input: str, user_input
        :param chatbot_response: str, chatbot_response
        """
        timestamp = datetime.now()  # Get the current timestamp
        formatted_timestamp = timestamp.strftime(
            "%Y-%m-%d %H:%M")  # Format the timestamp

        # Push the user input, chatbot response, and the timestamp to the Firebase database
        self.db_user_ref.push().set(
            {'user-input': user_input.upper(), 'chatbot-response': chatbot_response.upper(), "timestamp": formatted_timestamp})

    def get_all_user_interactions(self):
        """
        This function is used to get all the user interactions with the chatbot. 
        :return: dictionary of user interactions
        """
        return self.db_user_ref.get()

    def get_single_chatbot_response_from_user_input(self, user_input):
        """
        This function is used to get the chatbot response based on the user input. 
        :param user_input: str, user_input

        :return: list of chatbot response if match if found, otherwise 'No databse entry found!'
        """
        all_user_interactions = self.get_all_user_interactions()  # Get all the user interactions

        for key, value in all_user_interactions.items():
            # Check if there is a match for the user input
            if (value['user-input'] == user_input.upper()):
                # Return the chatbot response if a match is found
                return value['chatbot-response']

        # Return 'No databse entry found!' if no match found
        return 'No database entry found!'

    def get_multi_chatbot_response_from_user_input(self, user_input):
        """
        This function is used to get multiple chatbot response to the same user input if any. 
        :param user_input: str, user_input

        :return: list of chatbot responses
        """
        # Get all the user interactions
        all_user_interactions = self.get_all_user_interactions()
        chatbot_response_list = []  # Initialse chatbot response list

        for key, value in all_user_interactions.items():
            # Check if there is a match for the user input
            if (value['user-input'] == user_input.upper()):
                # Append the chatbot response to the list if a match is found
                chatbot_response_list.append(value['chatbot-response'])

        # Return the chatbot response if the list size if greater than 0, otherwise, return 'No database entry found!'
        return chatbot_response_list if len(chatbot_response_list) > 0 else 'No database entry found!'
