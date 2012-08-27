#! /usr/bin/python
'''
#=============================================================================
#     FileName:		client.py
#     Desc:	        socket simple client, send and recv message.	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-07-10 09:57:35
#     History:		
#=============================================================================
'''
import os
import socket  
import sys

s=socket.socket()  
s.connect(('localhost',50000)) 

while True:
    data = raw_input("---> ")
    if data == "quit" or not data:
        s.send(data)
        break

    s.send(data)

    back_data = s.recv(1024)  

    print back_data

s.close()  
