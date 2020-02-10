#Top-Level DNS 

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
