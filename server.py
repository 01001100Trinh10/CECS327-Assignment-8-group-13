#adam tim 028832685
#luke trinh 028243668
import time
import socket
from pymongo import MongoClient



myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a tcp socket
connectionLink = "mongodb+srv://adamtim2002:121002Tim@dd1.dffgo.mongodb.net/?retryWrites=true&w=majority&appName=DD1"
client = MongoClient(connectionLink)#connects to mongoDB database
database = client["test"]#loads database
collection1 = database["DD1_virtual"]

while True:
    try:
        #gets the server ip and port number
        serverIP= str(input("enter the server ip address:"))
        serverPort= int(input("enter the server port number:")) 
        try:
            #binds the server ip and port number
            myTCPSocket.bind((serverIP, serverPort))
            myTCPSocket.listen(5) #listens for incoming connections
            print(f'Server is listening on {serverIP}:{serverPort}')
            
            #accepts a new incoming connection
            incomingSocket, incomingAddress = myTCPSocket.accept()
            print(f'connection from {incomingAddress}')

            while True: 
                try:
                    #receives data from client
                    myData = incomingSocket.recv(1024)
                    #if no data is recieved
                    if not myData:
                        break
                    #decodes data
                    myData = myData.decode('utf-8')
                    print("message recieved: ", myData)
                    if myData == "1":
                        #query 1 - fetches the average moisture in the kitchen fridge
                        pipeline1 = [
                        { "$lookup": {"from": "DD1_metadata" , 
                        "localField": "payload.parent_asset_uid", 
                        "foreignField": "assetUid", 
                        "as": "data"}
                        }, #performs a join operation between the collection and the DD1_metadata collection
                        {"$match": {"data.customAttributes.additionalMetadata.location": "kitchen", 
                                    "data.customAttributes.name": {"$regex": "Fridge"}, 
                                    "payload.timestamp": {"$lt": str(time.time()), "$gt": str(time.time() - 10800)}}
                        }, #filters the data based on the objects location, name and is within the last 3 hours
                        {"$group": {"_id": "$payload.parent_asset_uid",
                                    "averageMoisture": {"$avg": {"$toDouble": "$payload.Moisture Meter - FridgeSensor"}}}
                        } #groups the data by the average moisture of the device
                        ]
                        results = collection1.aggregate(pipeline1)
                        for result in results:
                            moisture = result["averageMoisture"] #stores the results in a vairable
                            myData = f"The average moisture inside the kitchen fridge in the past 3 hours is {moisture}%"  #prints out the results
                    elif myData == "2":
                        #query 2 - finds average water consumption per cycle for the wash machine
                        pipeline2 = [
                        { "$lookup": {"from": "DD1_metadata" , 
                                    "localField": "payload.parent_asset_uid", 
                                    "foreignField": "assetUid", 
                                    "as": "data"}
                                    }, #performs a join operation between the collection and the DD1_metadata collection
                        {"$match": {"data.customAttributes.additionalMetadata.location": "kitchen", 
                                    "data.customAttributes.name": {"$regex": "Dishwasher"} }
                        },#filters the data based on the objects location and name
                        {"$group": {"_id": "$payload.parent_asset_uid",
                                    "averageWaterConsumption": {"$avg": {"$toDouble": "$payload.DishwasherWaterConsumptionSensor"}}}
                        } #groups the data by the average water consumption of the device
                        ]
                        results = collection1.aggregate(pipeline2)
                        for result in results:
                            waterConsumption = result["averageWaterConsumption"] #stores the results in a vairable
                            myData = f"The average water consumption per cycle is {waterConsumption}" #prints out the results
                    elif myData == "3": #query 3
                        pipeline3 =[
                            { "$lookup": {"from": "DD1_metadata" , 
                                    "localField": "payload.parent_asset_uid", 
                                    "foreignField": "assetUid", 
                                    "as": "data"}
                            }, #performs a join operation between the collection and the DD!_metadata collection
                            { "$addFields" : {"name" : "$data.customAttributes.name"}}, #adds the field name
                            {"$unwind": {"path": "$name"}}, #unwinds the name array
                            {
                            "$group" : {"_id" : "$name",
                                        "fridgeEnergy" : {"$sum" : {"$toDouble": "$payload.FridgeAmmeter"}},
                                        "DishWasherEnergy" : {"$sum" : {"$toDouble": "$payload.Dishwasherammeter"}},
                                        "Fridge2Energy" : {"$sum" : {"$toDouble": "$sensor 1 2e22eb50-56dc-433b-a25e-7ce35c6fb595"}}
                                        } 
                            }, # groups the fields by the total amount of energy they cnsume
                            { "$addFields" : {"energyConsumption" : {"$add": [{"$toDouble": "$fridgeEnergy"}, {"$toDouble": "$DishWasherEnergy"}, {"$toDouble": "$Fridge2Energy"}]}}},
                            #create an energy consumption field to create the list of energy consumption per device
                            {"$sort": {"energyConsumption" : -1}}, #sorts the consumption fields by greatest to least
                            {"$limit":1} #gets the device with the greatest energy consumption
                            ]
                        results = collection1.aggregate(pipeline3) #gets the results of the pipeline
                        for result in results:
                            identity = result["_id"] #stores the results in a vairable
                            energyConsumption = result["energyConsumption"]
                            myData = f"The device with the most energy consumption is {identity} with {energyConsumption} amps." #prints out the results
                    incomingSocket.send(bytearray(str(myData), encoding='utf-8'))
                except:
                    #connection is closed
                    print("connection has been closed")
                    incomingSocket.close()
                    break
            break
        except socket.error:
            #checks if the ip addresses and port number are able to connect
            print(f"Error: Unable to connect to the server at {serverIP}:{serverPort}")
            print("Please check the IP address and port number, and try again.")
    except:
        #checks if the inputs are correct
        print("Please check the IP address and port number, and try again.")
    
