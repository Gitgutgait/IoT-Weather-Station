
import paho.mqtt.client as mqtt
import json

class Publisher:
    def __init__(self, topic, client_id, broker, port):
        # Initialize the Publisher object with the given topic, client ID, broker, and port
        self.topic = topic
        self.client = mqtt.Client(client_id)
        self.client.connect(broker, port, 60)  # Connect to the MQTT broker


    def publish(self, data):
        # Publish the data as a JSON message to the specified topic
        self.client.publish(self.topic, json.dumps(data))

   

