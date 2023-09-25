
from FirebaseHandler import FirebaseHandler

firebase_handler = FirebaseHandler()

# Test - Temperature
# firebase_handler.save_temperature(20)
# print(firebase_handler.get_all_temperature_values())

# print(firebase_handler.get_single_temperature_value_at_time('2023-09-25 15:23'))
# print(firebase_handler.get_multi_temperature_values_at_time('2023-09-25 15:23'))

# print(firebase_handler.get_single_time_value_at_temperature(50))
# print(firebase_handler.get_multi_time_values_at_temperature(50))

# Test - Humidity
# firebase_handler.save_humidity(44)
# print(firebase_handler.get_all_humidity_values())

# print(firebase_handler.get_single_humidity_value_at_time('2023-09-25 15:28'))
# print(firebase_handler.get_multi_humidity_values_at_time('2023-09-25 15:28'))

# print(firebase_handler.get_single_time_value_at_humidity(44))
# print(firebase_handler.get_multi_time_values_at_humidity(52))

# Test - User
# firebase_handler.save_user_interaction('Hello Chatbot!', 'Hello User!')
# print(firebase_handler.get_all_user_interactions())

# print(firebase_handler.get_single_chatbot_response_from_user_input('Hello Mac!'))
# print(firebase_handler.get_multi_chatbot_response_from_user_input('Hello Chatbot!'))
