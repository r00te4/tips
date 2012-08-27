#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		server_epoll_tcp.py
#     Desc:	        A socket server can support epoll teck.	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-18 09:59:42
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
server_socket.setblocking(0)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

connects = {}
requests = {}
responses = {}

def accept_epoll():
    try:
        while True:
            client_socket, client_addr = server_socket.accept()
            client_socket.setblocking(0)
            print client_socket, client_addr
            epoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLHUP | select.EPOLLET)
            connects[client_socket.fileno()] = client_socket
            requests[client_socket.fileno()] = b''
            responses[client_socket.fileno()] = b''
    except socket.error:
        pass

def recv_epoll(sock):
    data = ''
    try:
        while True:
            buf = sock.recv(1024)
            if not buf:
                break
            data += buf
            print data
    finally:
        return data

def send_epoll(sock, data):
    try:
        while len(data) > 0:
            back_data = data + " finished! "
            bytes = sock.send(back_data)
            print "bytes: ", bytes
            data = data[bytes:]
    finally:
        return data

def do_request(fileno):
    requests[fileno] += recv_epoll(connects[fileno])
    request = requests[fileno]

    if request == "quit" or not request:
        print connects[fileno], "closed"
        connects[fileno].close()
    else:
        responses[fileno] = request
        epoll.modify(fileno, select.EPOLLOUT | select.EPOLLET)


def do_response(fileno):
    send_epoll(connects[fileno], responses[fileno])
    requests[fileno] = b''
    epoll.modify(fileno, select.EPOLLIN | select.EPOLLET)


def hup_epoll(fileno):
    epoll.unregister(fileno)
    connects[fileno].lose()
    del connects[fileno]
    del requests[fileno]
    del responses[fileno]


def do_epoll(fileno, event):
    try:
        if fileno == server_socket.fileno():
            accept_epoll()
        elif event & select.EPOLLIN:
            do_request(fileno)
        elif event & select.EPOLLOUT:
            do_response(fileno)
        elif event & select.EPOLLHUP:
            hup_epoll(fileno)
    except:
        raise

def close_epoll():
    epoll.unregister(server_socket.fileno())
    server_socket.close()
    epoll.close()


while True:
    events = epoll.poll()
    for fileno, event in events:
        do_epoll(fileno, event)

close_epoll()


