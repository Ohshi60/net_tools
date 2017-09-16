#imports
import socket
import threading

#declare variables
bind_ip = "0.0.0.0"
bind_port = 9999

#create a server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#tell the server where to listen
server.bind((bind_ip,bind_port))

#tell the server we want to listen with max 5 threads at a time
server.listen(5)

#print out a message to inform that server is running
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#the client handling thread 

def handle_client(client_socket):

  #print out what the client needs
  request = client_socket.recv(1024)

  print "[*] Received: %s" % request

  #send back a packet
  client_socket.send("ACK!")
  #close the connection
  client_socket.close()

#client loop

while True:
	
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])

	# spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()


