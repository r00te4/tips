#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#     FileName:		server_libevent.py
#     Desc:		    A socket server can support libevent function.
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-23 10:01:56
#     History:		
#=============================================================================
'''
import socket, signal, libevent

def callback_interrupt(signum, events, event_obj):
    libevent.loopExit(0)

def callback_onconnect(fd, events, event):
    # hack to avoid passing sock_srv from main()
    sock_srv = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
    sock, (host, port) = sock_srv.accept()
    conn = Connection(sock, (host, port))

class Connection:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.sock.setblocking(False)
        libevent.createEvent(sock, libevent.EV_READ, self.callback_onread).addToLoop()
    
    def callback_onread(self, fd, events, event_obj):
        buf = self.sock.recv(4096)
        if not buf: # just disconnect
            self.sock.close()
            return
        # Yeah, print!
        print "%r %r" % (self.addr, buf)
        self.sock.send("finished")
        # reuse current event
        event_obj.addToLoop()

if __name__ == '__main__':
    # bind.
    sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_srv.setblocking(False)
    sock_srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_srv.bind(('localhost', 50000))
    sock_srv.listen(5)
    
    libevent.createSignalHandler(signal.SIGINT, callback_interrupt).addToLoop()
    libevent.createEvent(sock_srv, libevent.EV_READ|libevent.EV_PERSIST, callback_onconnect).addToLoop()
    libevent.dispatch()
