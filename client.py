#client
#Use PROJI-DNSRS.txt and PROJI-DNSTS.txt for tables 
#Use PROJI-HNS.txt for searches
#If "A" return else check TS if still NS return error 
#DNS entry/host name are MAX 200 chars 
#DNS look ups are case insensitive 

#python client.py rsHostname rsListenPort tsListenPort
#rsHostname argv[1]

import sys
import os
import time
import random
import socket


try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
        
# Define the port on which you want to connect to the server
#rsListenPort = int(sys.argv[2])
tsListenPort = int(sys.argv[3])
localhost_addr = socket.gethostbyname(socket.gethostname())
# connect to the server on local machine

#rsServer_binding = (localhost_addr, rsListenPort)
tsServer_binding = (localhost_addr, tsListenPort)
#cs.connect(rsServer_binding)
cs.connect(tsServer_binding)

msg = cs.recv(1024)
print("[C]: Data received from server: {}".format(msg.decode('utf-8')))
cs.close()
exit()


