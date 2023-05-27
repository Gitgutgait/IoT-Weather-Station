from flask import Flask, jsonify, render_template
from subscriber import *
from model import *

class Controller:
    def __init__(self):
        # Create an instance of the Model class
        self.model = Model()    
        # Create an instance of the Subscriber class with the model's update_datastore method as a callback
        self.subscriber = Subscriber(self.model.update_datastore)

    def get_data(self):
        # Retrieve data from the model
        return self.model.get_data() 
