#imports 
import socket
import sys
import getopt
import threading
import subprocess


#define global variables
listen			= False
command			= False
upload 			= False
execute			= ""
target			= ""
upload_destination 	= ""
port			= 0

def usage():
	print "BHP Net Tool"
	print
	print "Usage netclone.py -t target_host -p port"
	print "-l --listen			- listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_run		- execute the given file upon receiving a connection"
	print ""

usage()
