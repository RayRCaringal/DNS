#Top-Level DNS 

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
    hostName = reply.decode('utf-8')
    print ("[TS]: Request from a client for hostname " + hostName)
    if hostName in table:
        print ("[TS]: Hostname " + hostName + " found sending IP Address to Client")
        clientsocket.send((table.get(hostName).ip).encode('utf-8'))
    else: 
        print ("[TS]: Hostname " + hostName + " not found")
        error = "Error:HOST NOT FOUND"
        clientsocket.send(error.encode('utf-8'))

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
    print("[TS]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()
server_binding = ('', int(sys.argv[1]))
ss.bind(server_binding)

#Listen forever 
msg = "[TS] Connected to Top-Level DNS"
while True:
    ss.listen(5)
    clientsocket, addr = ss.accept()
    print ("[TS]: Got a connection request from a client at {}".format(addr))
    #Acknowledgement 
    clientsocket.send(msg.encode('utf-8'))
    newThread = threading.Thread(target=run)
    newThread.start()


ss.close()
exit()