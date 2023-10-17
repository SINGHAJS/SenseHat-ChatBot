"""
@Ussage Guide
#1 Import and create an instance of the CloudDatabaseUpdateScheduler class

@explanation
    The code below creates an instance of the CloudDatabaseUpdateScheduler class. When 
    creating an instance of this class, the local and remote datbase instances must be 
    passed as the parameters. You can additionally provide a timer param which controls
    when the scheduler will push local databse changes to the databse. The default timer
    value is 86400 secs which is 24 hours. 

<code> 
    from database.CloudDatabaseUpdateScheduler import CloudDatabaseUpdateScheduler
    scheduler = CloudDatabaseUpdateScheduler(local_database, cloud_database, 5)
</code>

#2 Now start the scheduler to update the cloud databse with the local databse

@explanation
    The below code will start the scheduler and when the timer reaches it specified 
    value, it will push local databse changes to the cloud databse.

<code> 
    def start_cloud_database_scheduler()
</code>

"""