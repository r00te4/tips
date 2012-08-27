#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		server_fork_tcp.py
#     Desc:	        A socket server can support fork function	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-01 10:00:47
#     History:		
#=============================================================================
'''

import os
import socket  
import sys
import time
import signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50000))
s.listen(0)

while True:
    client_socket, client_addr = s.accept()
    print "Connected from: ", client_addr, "client_socket: ", client_socket

    pid = os.fork()

    if pid:
        client_socket.close()
        continue
    else:
        s.close()
        while True:
            data = client_socket.recv(1024)
            print data
            if not data:
                break
            pid_2 = os.fork()
            if pid_2 == 0:
                if data == "gedit":
                    os.popen("/usr/bin/gedit &")
                    client_socket.send("gedit finished")
                if data == "nautilus":
                    os.popen("/usr/bin/nautilus")
                    client_socket.send("nautilus finished")
                else:
                    back_data = data+" finished"
                    client_socket.send(back_data)
                #os._exit(0)
        client_socket.close()
        os._exit(0)

