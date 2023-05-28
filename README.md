# IoT Weather Station

Welcome to the IoT Weather Station! A project realized in the course ”Internet Of Things” at Aarhus University in 2023. This Markdown document will guide you through the setup and usage of the weather station system.

## Prerequisites

Before starting, ensure that you have the following components connected:

- Raspberry Pi
- SensorHat

## Installation

1. Clone the source code repository for the IoT Weather Station by running the following command:

```bash
$ git clone https://github.com/Gitgutgait/IoT-Weather-Station.git
```

2. Navigate to the project directory on your Raspberry Pi.

```bash
$ cd IoT-Weather-Station
```

3. Install the necessary Python libraries by running the following command:

```bash
$ pip3 install Flask==2.3.2 paho-mqtt==1.6.1 sense-hat==2.4.0
```

## Usage

To run the IoT Weather Station project, follow the steps below:

1. In the project directory, navigate to the WeatherStation directory and execute the following command:

```bash
$ python3 controller.py
```

2. In the same project directory, navigate to the WebServer directory and run the following command:

```bash
$ python3 webApp.py
```

3. Open a web browser and visit the following address: [http://127.0.0.1:5001/](http://127.0.0.1:5001/)
   * To view the data format or directly retrieve data, go to http://127.0.0.1:5001/fetch_data

## Important Notes

- The average temperature will first appear after the 10th iteration of data fetch.
- Please note that the temperature displayed might not indicate the precise current temperature in the room. This discrepancy is due to the sensors being placed closely to the Raspberry Pi, which can generate heat and provide inaccurate readings.