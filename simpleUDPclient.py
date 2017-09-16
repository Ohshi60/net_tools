#import modules

import socket

#declare variables

target_host = "127.0.0.1"
target_port = 80

#Create a client

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Send some data

client.sendto("AAABBBCCC",(target_host,target_port))

#Receive some data

data, addr = client.recvfrom(4096)
#Print the response

print data

