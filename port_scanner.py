#!/bin/py

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2 :
	target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPV4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("_" *50)
print("Scanning Target "+target)
print("Time Started :"+str(datetime.now()))
print("_"*50)

try:
 for port in range (1,65535):
 	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 	socket.setdefaulttimeout(1)
 	result=s.connect_ex((target,port))  #returns a port indicator
 	#print("Checking Port{}".format(port))
 	if result ==0 :
 		print("Port{} is open".format(port))
 	s.close()
 	
except KeyboardInterrupt:
 	print("\nExiting program")
 	sys.exit()
except socket.gaierror:
 	print("Hostname could not be resolved")
 	sys.exit()
except socket.error:
 	print("Couldnt connect to server")
 	sys.exit()

finally:
    print("_" * 50)
    print("Scan completed at: " + str(datetime.now()))
    print("_" * 50)



