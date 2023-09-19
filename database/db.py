from SQLiteDatabaseHandler import SQLiteDatabaseHandler

sqlite_handler = SQLiteDatabaseHandler()
sqlite_handler.establish_db_connection()

# Test - Temperature Table
sqlite_handler.create_temp_table()
sqlite_handler.insert_into_temp_table(20.0)
sqlite_handler.insert_into_temp_table(40.0)
sqlite_handler.insert_into_temp_table(10.0)
sqlite_handler.get_temperature_readings()

# Test - Humidity Table
sqlite_handler.create_humidity_table()
sqlite_handler.insert_into_humidity_table(11.0)
sqlite_handler.insert_into_humidity_table(12.0)
sqlite_handler.insert_into_humidity_table(13.0)
sqlite_handler.get_humidity_readings()

sqlite_handler.terminate_db_connection()
