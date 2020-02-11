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
    cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
        
# Define the port on which you want to connect to the server
rsListenPort = int(sys.argv[2])
tsListenPort = int(sys.argv[3])
localhost_addr = socket.gethostbyname(socket.gethostname())


rsServer_binding = (localhost_addr, rsListenPort)
tsServer_binding = (localhost_addr, tsListenPort)

print(rsServer_binding)
print(tsServer_binding)

#Connect to Root Server first 
cs.connect(rsServer_binding)


#Use cs.connect(tsServer_binding) to switch connection when necessary 

msg = cs.recv(1024)
print("[C]: Data received from server: {}".format(msg.decode('utf-8')))

"""
[REDACTED] We might need it so I'm leaving it 
Temporary solution for switching sockets 
cs.close()
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = msg.decode('utf-8').split()[0]
if flag == "[RS]":
    cs.connect(tsServer_binding)
else:
    cs.connect(rsServer_binding)

"""

#Nvm this method works
cs2.connect(tsServer_binding)
msg = cs2.recv(1024)
print("[C]: Data received from server: {}".format(msg.decode('utf-8')))
cs.close()
exit()


