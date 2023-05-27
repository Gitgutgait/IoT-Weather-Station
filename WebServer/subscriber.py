import paho.mqtt.client as mqtt
import json
from datastore import DataStore

class Subscriber:
    def __init__(self, arg_update_datastore):
        # Create an instance of the MQTT client
        self.client = mqtt.Client()  
        
        # Assign the provided arg_update_datastore to the update_datastore attribute
        self.update_datastore = arg_update_datastore  

        # Set the on_connect callback function
        self.client.on_connect = self.on_connect
        # Set the on_message callback function  
        self.client.on_message = self.on_message  
        
         # Connect to the MQTT broker
        self.client.connect("test.mosquitto.org", 1883, 60) 

        # Start the loop in a new thread for handling network communication
        self.client.loop_start()  

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribe to the "weather_station" topic
        self.client.subscribe("weather_station")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        # Parse the incoming JSON message
        data = json.loads(msg.payload.decode('utf-8'))  
        print(f"Received data: {data}") 
        
        # Call the provided update_datastore callback function with the received data
        self.update_datastore(data)  
