#adam tim 028832685
import socket

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
                    myData = myData.upper()
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
    
