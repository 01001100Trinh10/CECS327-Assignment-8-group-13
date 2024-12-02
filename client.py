#adam tim 028832685
import socket

while True:
    try:
        #gets the server ip and port number
        serverIP= str(input("enter the server ip address:"))
        serverPort= int(input("enter the server port number:"))

        try:
            #creats a tcp socket
            myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connects to the server
            myTCPSocket.connect((serverIP, serverPort)) 

            while True:
                #user inputs a message to send
                someData = str(input("enter a message to send: "))
                myTCPSocket.send(bytearray(str(someData), encoding='utf-8'))
                #client recieves a message back
                serverResponse = myTCPSocket.recv(1024)

                print(serverResponse.decode('utf-8'))
                #allows the user to send multiple messages
                condition = input("do you want to exit, type y/n: ")
                if condition.lower() == "y":
                    break
            myTCPSocket.close() #closes the socket
            break
        #checks if the client is able to connect
        except socket.error:
            print(f"Error: Unable to connect to the server at {serverIP}:{serverPort}")
            print("Please check the IP address and port number, and try again.")
    #checks if the ip address and port are valid formats
    except:
        print("Please check the IP address and port number, and try again.")



