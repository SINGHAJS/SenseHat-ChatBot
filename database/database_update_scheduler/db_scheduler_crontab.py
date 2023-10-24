from database.database_update_scheduler.CloudDatabaseUpdateScheduler import CloudDatabaseUpdateScheduler
from database.cloud_database.FirebaseHandler import FirebaseHandler
from database.local_database.SQLiteDatabaseHandler import SQLiteDatabaseHandler

sqlite_handler = SQLiteDatabaseHandler()
sqlite_handler.establish_db_connection()
firebase_handler = FirebaseHandler()

scheduler = CloudDatabaseUpdateScheduler(sqlite_handler, firebase_handler)
scheduler.push_local_db_data_cloud()