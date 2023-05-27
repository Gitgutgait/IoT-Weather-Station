from publisher import Publisher
from model import Model
import paho.mqtt.client as mqtt
import json, time

class Controller:
    def __init__(self, lat=56.150369, long=56.172070):
        # Create an instance of the Publisher class to publish MQTT messages
        self.publisher = Publisher("weather_station", "WeatherStation", "test.mosquitto.org", 1883)
        # Create an instance of the ModelClass
        self.model = Model()  
        # List of latitude and longitude values
        self.latitude_AarhusC_N_S = [56.150369, 56.172070,56.098782] 
    
        self.longitude_AarhusC_N_S = [10.200882, 10.191330, 10.219030]  
    
    def process_data(self):
        # Fetch data using the fetch_data() method from the ModelClass
        data = self.model.sense_hat_data.fetch_data()
        
        # Add latitude and longitude values to the data dictionary
        data["latitude"] = self.latitude_AarhusC_N_S[0]
        data["longitude"] = self.longitude_AarhusC_N_S[0]
        
        # Publish the data dictionary as a JSON message
        self.publisher.publish(data)
        

if __name__ == '__main__':
    # Create an instance of the Controller class
    controller = Controller()  
    
    while True:
        # Call the process_data() method of the controller to process and publish data
        controller.process_data()
        
        # Sleep for 5 seconds before processing the next set of data
        time.sleep(2)
