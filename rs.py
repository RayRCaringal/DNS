#RS

import sys
import os
import time
import random
import socket
import threading

#Stores Flag and Ip so it can be used in Key:Value pair dict 
class vals:
    def __init__(self,ip, flag):
        self.ip = ip
        self.flag = flag


def run():
    clientsocket.send(msg.encode('utf-8'))
    reply = clientsocket.recv(1024)
    print(reply.decode('utf-8'))

    

#Creates Table 
table = {}
path = os.path.dirname(os.path.realpath('__file__')) + '\PROJI-DNSRS.txt' 
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
#Listen forever 
msg = "[RS] Connected to Root DNS"
while True:
    ss.listen(5)
    clientsocket, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    newThread = threading.Thread(target=run)
    newThread.start()
    

ss.close()
exit()