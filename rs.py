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
    EOF = 1
    while EOF is not 0:
        print("[RS]: Waiting on Client")
        reply = clientsocket.recv(1024)
        hostName = reply.decode('utf-8').rstrip().casefold()
        if hostName =="eof":
            print ("[RS]: Exiting client at {}".format(addr))
            return 
        print ("[RS]: Request from a client for hostname " + hostName)
        if hostName in table:
            if table.get(hostName).flag is 'A':
                print ("[RS]: Hostname " + hostName + " found sending IP Address " +table.get(hostName).ip+ " to Client")
                clientsocket.send((table.get(hostName).ip).encode('utf-8'))
            else:
                print ("[RS]: Hostname " + hostName + " not found returning Top-Level DNS Address")
                clientsocket.send(NSFlag.encode('utf-8'))
        else: 
            print ("[RS]: Hostname " + hostName + " not found returning Top-Level DNS Address")
            clientsocket.send(NSFlag.encode('utf-8'))


#Creates Table 
table = {}
NSFlag = "[NS] "
path = os.path.dirname(os.path.realpath('__file__')) + '\PROJI-DNSRS.txt' 
if os.path.isfile(path):
    with open(path, 'r') as f:
        for line in f:
            items = line.split()
            if items[2] is 'A':
                val = vals(items[1], items[2])
                table[items[0]] = val
            else:
                NSFlag += items[0]

#Example on how to retrieve ip and flag 
#print(table.get("grep.cs.princeton.edu").ip)
#print(table.get("grep.cs.princeton.edu").flag)
    

#Create Server Socket
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[RS]: Server socket created")
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
    print ("[RS]: Got a connection request from a client at {}".format(addr))
    newThread = threading.Thread(target=run)
    newThread.start()
    
ss.close()
exit()