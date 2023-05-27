class DataStore:
    def __init__(self):
        # Initialize an empty dictionary to store data
        self.data = {}  

    def update_datastore(self, new_data):
        # Update the data in the data store with the new data
        self.data = new_data 

    def get_data(self):
        # Retrieve and return the current data stored in the data store
        return self.data  

