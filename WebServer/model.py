from datastore import *  # Import the DataStore class

class Model:
    def __init__(self):
        # Create an instance of the DataStore class
        self.data_store = DataStore()  

    def update_datastore(self, new_data):
        # Update the data store by calling the DataStore's update_datastore method
        return self.data_store.update_datastore(new_data)  

    def get_data(self):
         # Retrieve data from the data store by calling the DataStore's get_data method
        return self.data_store.get_data() 

    