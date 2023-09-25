from SQLiteDatabaseHandler import SQLiteDatabaseHandler

sqlite_handler = SQLiteDatabaseHandler()
sqlite_handler.establish_db_connection()

# Test - Temperature Table
# sqlite_handler.create_temp_table()
# sqlite_handler.insert_into_temp_table(20.0)
# sqlite_handler.insert_into_temp_table(40.0)
# sqlite_handler.insert_into_temp_table(101.0)
# sqlite_handler.get_temperature_readings()
# print(sqlite_handler.get_temperature_reading_at_time('2023-09-25 07:00:07'))
# print(sqlite_handler.get_time_reading_at_temperature(90))

# Test - Humidity Table
# sqlite_handler.create_humidity_table()
# sqlite_handler.insert_into_humidity_table(11.0)
# sqlite_handler.insert_into_humidity_table(12.0)
# sqlite_handler.insert_into_humidity_table(13.0)
# sqlite_handler.get_humidity_readings()

# print(sqlite_handler.get_humidity_reading_at_time('2023-09-19 05:01:11'))
# print(sqlite_handler.get_time_reading_at_humidity(13))

# Test - User Table
# sqlite_handler.create_user_table()
# sqlite_handler.insert_into_user_table('Hello world', 'Hello user')
# sqlite_handler.get_user_readings()
# print(sqlite_handler.get_chatbot_response_from_user_input('Hello someone'))

sqlite_handler.terminate_db_connection()
