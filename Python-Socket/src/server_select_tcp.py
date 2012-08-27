#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		server_select_tcp.py
#     Desc:	        A socket server can support select tech.	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-10 10:03:38
#     History:		
#=============================================================================
'''

import os, sys
import socket, select

host = "localhost"
port = 50000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

r_list =[server_socket]
w_list = []
e_error = []

while True:
    try:
        input, output, error = select.select(r_list, w_list, e_error)
    except select.error, e:
        break

    for sock in input:
        if sock is server_socket:
            client_socket, client_addr = server_socket.accept()
            print "Connected: ", client_socket, client_addr
            #client_sock.setblocking(0)
            r_list.append(client_socket)
        else:
            msg = sock.recv(1024)
            if len(msg):
                print "MSG: ", msg
                back_data = msg + " FeedBack MSG"
                sock.send(back_data)
            else:
                print sock, " QUIT"
                r_list.remove(sock)
                sock.close()

server_socket.close()

