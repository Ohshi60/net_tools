import socket

target_host = "0.0.0.0"
target_port = 9999 

#Create a client socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect the client

client.connect((target_host,target_port))

#Send some data
message = "This message is for you"
client.send(message)

#Receive some data
response = client.recv(4096)

#Print the response

print response
