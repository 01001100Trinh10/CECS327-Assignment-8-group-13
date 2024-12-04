# CECS327-Assignment-8
Adam Tim
Luke Trinh
Malik Luti
Assignment 8
CECS 327 Sec 02
8 December 2024

**INSTRUCTIONS TO RUN CLIENT, SERVER, AND DATABASE**
Things you to run an end-to-end IoT system:
    - Google Cloud (With Python installed)
    - Dataniz account    
    - MongoDB
    - Python interpreter
    - system.py
    - client.py

**Google Cloud Setup**
In this lab, we had two distinct virtual machines(VMs) running in Google Cloud. One VM will represent the client that communicates with the server and the other VM will represent the server that fetches data from MongoDB from a set of pre-coded queries. (TALK ABOUT IPs)

**Dataniz Setup**
Before accessing the data, we need to first generate and store data. We will use Dataniz to simulate IoT devices that will generate data from sensors that we created. First, we started with creating three IoT Devices:
1. Smart Fridge: A virtual device that represents a smart IoT-enabled refrigerator. The fridge will include a WiFi-enabled board (we used a Raspberry Pi), an ammeter sensor, a thermistor sensor, and a moisture sensor.
2. Smart Dishwater: A vitrual device that represents a smart IoT-enabled dishwasher. The dishwasher will include a WiFi-enabled board (also used a Raspberry Pi), an ammerter sensor, and a water consumption sensor.
3. Smart Fridge (duplicate): A virtual device that represents another smart IoT-enabled refrigerator. The fridge will be a duplicated device with identical components to the smart fridge mentioned before.

Afterwards, we created a Message Queuing Telemetry Transpot (MQTT) broker through dataniz. The role of the MQTT broker is to receive data from the IoT devices and send over that data to the client subscribed to the broker (that being the database).

Lastly, we (TALK ABOUT METADATA HERE)

**MongoDB Setup**
Next, we set up a basic MongoDB server that takes in the data received from the MQTT broker and stores it. Here, we will be fetching the data from this server using queries from pyMongo.

**Compiling the code**

