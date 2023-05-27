from sense_hat import SenseHat
import time

class SenseHatData:
    def __init__(self):
        # Instantiate the SenseHat sensor
        self.sense = SenseHat()
        # Data buffer for analytic function
        self.data_buffer = []
        # Size of the buffer for moving average
        self.buffer_size = 10  

    def fetch_data(self):
        #Using sense() to fetch the data from the senseHat
        temperature = round(self.sense.get_temperature(), 2)
        humidity = round(self.sense.get_humidity(), 2)
        pressure = round(self.sense.get_pressure(), 2)


        if temperature >= 34:
            color = (255, 0, 0)  # red
        elif temperature <= 33:
            color = (0, 0, 255)  # blue
        else:
            color = (0, 255, 0)  # green
            # show the temperature on the senseHat display, shows in different color according to the values
        self.sense.show_message(str(temperature), text_colour=color)

        # Insert the needed value to a ist
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "buffer_size": self.buffer_size,
        }

        # calculate the average temperature for 10 day
        self.data_buffer.append(data['temperature'])
        if len(self.data_buffer) > self.buffer_size:
            self.data_buffer.pop(0)  # remove oldest value
            data['avg_temperature'] = round(sum(self.data_buffer) / self.buffer_size, 2)

        return data
