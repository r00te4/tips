#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		server_none_tcp.py
#     Desc:	        A simple socket server.	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-25 10:02:44
#     History:		
#=============================================================================
'''

import os, sys
import socket

host = "localhost"
port = 50000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

while True:
    client_socket, client_addr = server_socket.accept()
    print "Connect From: ", client_socket, client_addr

    while True:
        data = client_socket.recv(1024)
        print data
        if data == "quit" or not data:
            break

        back_data = data + " Finished!"
        client_socket.send(back_data)
    client_socket.close()

server_socket.close()
