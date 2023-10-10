
@Ussage Guide
#1 Import and create an instance of the SQLiteDatabaseHandler class

@explanation
    The code below creates an instance of the SQLiteDatabaseHandler class. This will 
    be used to use the functions provided by the SQLiteDatabaseHandler class.

<code> 
    from SQLiteDatabaseHandler import SQLiteDatabaseHandler
    sqlite_handler = SQLiteDatabaseHandler()
</code>

#2 Establish a connection with the local database using the establish_db_connection() 
   function. 

@explanation
    The code below uses the establish_db_connection() function to establish a 
    connection to the SQLite database. 

<code> 
   sqlite_handler.establish_db_connection()
</code>

#3 Create the necessary tables to store the data

@explanation
    The code below creates the tables in the database if they are not already ceated. To
    store the data, use these functions to create the tables. 

<code> 
    sqlite_handler.create_temp_table()
    sqlite_handler.create_humidity_table()
</code>

#4 Once the table is created, you can then insert and get records from the tables. 

@explanation
    The below code inserts entries into the created tables and gets the stored values. 

<code>
    sqlite_handler.insert_into_temp_table(temperature_value: double)
    sqlite_handler.get_temperature_readings() : list
    sqlite_handler.get_temperature_reading_at_time(time: str) : list
    sqlite_handler.get_time_reading_at_temperature(temperature: int) : list

    sqlite_handler.insert_into_humidity_table(humidity_value: double)
    sqlite_handler.get_humidity_readings() : list
    sqlite_handler.get_humidity_reading_at_time(time: str) : list
    sqlite_handler.get_time_reading_at_humidity(humidity: int) : list

    sqlite_handler.insert_into_user_table(user_input: str, chatbot_response: str)
    sqlite_handler.get_user_interaction_data() : list
    sqlite_handler.get_chatbot_response_from_user_input(user_input: str) : list
</code>

#5 Terminate the database connection once done

@explanation 
    The below code terminates the cursor and database connection. 

<code>
    sqlite_handler.terminate_db_connection()
</code>
