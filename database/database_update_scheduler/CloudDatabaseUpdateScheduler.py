import time
import logging


class CloudDatabaseUpdateScheduler:

    def __init__(self, local_databse, cloud_databse, timer=86400):
        self.local_databse = local_databse
        self.cloud_databse = cloud_databse
        self.is_db_scheduler_started = False
        self.timer = timer

    def start_cloud_database_scheduler(self):
        """        
        This function continuously runs and after the time specified is over, this function 
        will push the local databse changes to the cloud database. 
        """
        self.is_db_scheduler_started = True
        while self.is_db_scheduler_started:
            time.sleep(self.timer)
            local_temperature_data = self.local_databse.get_temperature_readings()
            local_humidity_data = self.local_databse.get_humidity_readings()
            local_user_interaction_data = self.local_databse.get_user_interaction_data()

            self.cloud_databse.push_local_temprature_date_to_cloud(
                local_temperature_data)
            self.cloud_databse.push_local_humidity_date_to_cloud(
                local_humidity_data)
            self.cloud_databse.push_local_user_interactions_date_to_cloud(
                local_user_interaction_data)

            print('Pushing Local Data to Cloud Database ...')

    def stop_cloud_database_scheduler(self):
        """
        This function is used to stop the cloud database scheduler.
        """
        self.is_db_scheduler_started = False
        logging.info('Stopping Cloud Database Scheduler')

    def push_local_db_data_cloud(self):
        """        
        This function is used by crontab to push the local database changes to the cloud database. 
        """
        local_temperature_data = self.local_databse.get_temperature_readings()
        local_humidity_data = self.local_databse.get_humidity_readings()
        local_user_interaction_data = self.local_databse.get_user_interaction_data()

        self.cloud_databse.push_local_temprature_date_to_cloud(
            local_temperature_data)
        self.cloud_databse.push_local_humidity_date_to_cloud(
            local_humidity_data)
        self.cloud_databse.push_local_user_interactions_date_to_cloud(
            local_user_interaction_data)
