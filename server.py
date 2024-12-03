#adam tim 028832685
#luke trinh 028243668
import time
import socket
from pymongo import MongoClient

connectionLink = "mongodb+srv://adamtim2002:121002Tim@dd1.dffgo.mongodb.net/?retryWrites=true&w=majority&appName=DD1"
client = MongoClient(connectionLink)
database = client["test"]
collection1 = database["DD1_virtual"]

myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a tcp socket
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
                    #changes data to upper case
                    if myData == "1":
                        pipeline1 = [
                        { "$lookup": {"from": "DD1_metadata" , 
                        "localField": "payload.parent_asset_uid", 
                        "foreignField": "assetUid", 
                        "as": "meta"}
                        },
                            {"$match": {"meta.customAttributes.additionalMetadata.location": "kitchen", 
                                        "meta.customAttributes.name": {"$regex": "Fridge"}, 
                                        "payload.timestamp": {"$lt": str(time.time()), "$gt": str(time.time() - 10800)}}
                            },
                            {"$group": {"_id": "$payload.parent_asset_uid",
                                        "avgMoisture": {"$avg": {"$toDouble": "$payload.Moisture Meter - FridgeSensor"}}}
                            }
                        ]
                        results = collection1.aggregate(pipeline1)
                        for result in results:
                            myData = f"The average moisture inside the kitchen fridge in the past 3 hours is {result["avgMoisture"]}%"       
                    #sends back data to client

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
    
