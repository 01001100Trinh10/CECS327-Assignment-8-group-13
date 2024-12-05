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

Afterwards, we created a Message Queuing Telemetry Transpot (MQTT) broker through dataniz. The role of the MQTT broker is to receive data from the IoT devices and send over that data to the client subscribed to the broker (that being the database). The broker will send data gathered from the sensors into the database.

Lastly, we added MetaData to the IoT devices to differentiate and select between devices. More specifically, we used location (longitude and latitude) to fetch specific device information. For example, we can differentiate between the two fridges as one is assigned to the kitchen but the other is garage.

**MongoDB Setup**
Next, we set up a basic MongoDB server that takes in the data received from the MQTT broker and stores it. Here, we will be fetching the data from this server using queries from pyMongo. We also established a connection with our server.py file to display data later on.

**Compiling the code**
Lastly, we compile the code from system.py and client.py onto separate Google Cloud VMs to create an end-to-end IoT system. Before compiling the code, we made adjustments to the server and client file.

**Setup for server.py**
Just like from assignment 6, the server will first need to set up the port ID and IP for the client to connect to. Afterwards, the server will wait until there is a valid connection from the client. Once there is a valid connection, the server will then await an input 1-4 which correspond to the following queries:
1. What is the average moisture inside my kitchen fridge in the past three hours?
2. What is the average water consumption per cycle in my smart dishwasher?
3. Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?
4. Exit

**Setup for client.py**
The user will be prompted to enter the external IP for the VM that contains the server.py file and the port number the server.py file set up. The main change we made for client.py compared to the previous version from assignment 6 was that we changed the communication from the user to the system. Instead of typing a message, the user will be prompted to choose 1 of 4 queries as mentioned above. If the user enters an incorrect input, the user will be prompted to try again. The client will run until the user chooses option 4 to exit.
