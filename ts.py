#Top-Level DNS 

import sys
import os
import time
import random
import socket

#Stores Flag and Ip so it can be used in Key:Value pair dict 
class vals:
    def __init__(self,ip, flag):
        self.ip = ip
        self.flag = flag

#Creates Table 
table = {}
path = os.path.dirname(os.path.realpath('__file__')) + '\PROJI-DNSTS.txt' 
if os.path.isfile(path):
    with open(path, 'r') as f:
        for line in f:
            items = line.split()
            val = vals(items[1], items[2])
            table[items[0]] = val

#Example on how to retrieve ip and flag 
#print(table.get("grep.cs.princeton.edu").ip)
#print(table.get("grep.cs.princeton.edu").flag)

#Create Server Socket
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()
server_binding = ('', int(sys.argv[1]))
ss.bind(server_binding)
ss.listen(5)

#Listen forever 
msg = "Connected to Top-Level DNS"
while True:
    clientsocket, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    clientsocket.send(msg.encode('utf-8'))


ss.close()
exit()