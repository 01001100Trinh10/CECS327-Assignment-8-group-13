#adam tim 028832685
#luke trinh 028243668
import socket

while True:
    try:
        #gets the server ip and port number
        serverIP= str(input("Enter the following numbers that respond to the queries:"))
        serverPort= int(input("enter the server port number:"))

        try:
            #creates a tcp socket
            myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connects to the server
            myTCPSocket.connect((serverIP, serverPort)) 

            while True:
                #user inputs a message to send
                someData = str(input("Enter a number to enter the following queries:\n1. What is the average moisture inside my kitchen fridge in the past three hours?\n2. What is the average water consumption per cycle in my smart dishwasher?\n3. Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?"))
                if someData == "1" and someData == "2" and someData == "3":
                    myTCPSocket.send(bytearray(str(someData), encoding='utf-8'))
                    #client recieves a message back
                    serverResponse = myTCPSocket.recv(1024)

                    print(serverResponse.decode('utf-8'))
                    #allows the user to send multiple messages
                    condition = input("do you want to exit, type y/n: ")
                    if condition.lower() == "y":
                        break
                else:
                    print("Sorry, this query cannot be processed. Try entering a number from one of the 3 queries")
            myTCPSocket.close() #closes the socket
            break
        #checks if the client is able to connect
        except socket.error:
            print(f"Error: Unable to connect to the server at {serverIP}:{serverPort}")
            print("Please check the IP address and port number, and try again.")
    #checks if the ip address and port are valid formats
    except:
        print("Please check the IP address and port number, and try again.")



