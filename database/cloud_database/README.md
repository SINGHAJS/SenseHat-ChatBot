"""
@Ussage Guide
#1 Import and create an instance of the FirebaseHandler class

@explanation
    The code below creates an instance of the FirebaseHandler class. This will 
    be used to use the functions provided by the FirebaseHandler class.

<code> 
    from database.FirebaseHandler import FirebaseHandler
    firebase_handler = FirebaseHandler() # Creating an instace of the FirebaseHandler
</code>

#2 Now you can use the functions offered by the FirebaseHandler class

@explanation
    Below is a list of functions offered by the FirebaseHandler class.

<code> 
    # Temperature
    firebase_handler.save_temperatre(temperature_value: int)
    firbase_handler.get_all_temperature_values() : dictionary
    firebase_handler.get_single_temperature_value_at_time() : int
    firebase_handler.get_multi_temperature_value_at_time() : list
    firebase_handler.get_single_time_value_at_temperature() : str
    firebase_handler.get_multi_time_value_at_temperature() : list
    firebase_handler.push_local_temprature_date_to_cloud(temperature_data: list)

    # Humidity
    firebase_handler.save_humidity(humidity_value: int)
    firbase_handler.get_all_humidity_values() : dictionary
    firebase_handler.get_single_humidity_value_at_time() : int
    firebase_handler.get_multi_humidity_value_at_time() : list
    firebase_handler.get_single_time_value_at_humidity() : str
    firebase_handler.get_multi_time_value_at_humidity() : list
    firebase_handler.push_local_humidity_date_to_cloud(humidity_data: list)

    #User 
    firebase_handler.save_user_interaction(user_input: str, chatbot_response: str)
    firebase_handler.get_all_user_interactions(): list
    firebase_handler.get_single_chatbot_response_from_user_input(user_input: str) : list
    firebase_handler.get_multi_chatbot_response_from_user_input(user_input: str) : list
    firebase_handler.self.db_local_user_interactions_data_ref(user_interaction_data : list)
</code>

@Troubleshooting
    If an error is encountered, please ensure the firebase_admin package is installed. 
    Also, ensure that the FirebasHandler class is being imported correctly.
"""