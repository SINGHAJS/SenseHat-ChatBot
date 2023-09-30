from CloudDatabaseUpdateScheduler import CloudDatabaseUpdateScheduler
from FirebaseHandler import FirebaseHandler
from SQLiteDatabaseHandler import SQLiteDatabaseHandler

sqlite_handler = SQLiteDatabaseHandler()
sqlite_handler.establish_db_connection()
firebase_handler = FirebaseHandler()

scheduler = CloudDatabaseUpdateScheduler(sqlite_handler, firebase_handler, 5)
scheduler.start_cloud_database_scheduler()
