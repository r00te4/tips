#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		server_thread_tcp.py
#     Desc:		    A socket server can support thread tech.
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-15 10:04:27
#     History:		
#=============================================================================
'''
import sys
import os
import socket
import threading
import Queue

class Mythread(threading.Thread):
    def run(self):
        print "The Thread name is: ", self.getName()
        while True:
            # 从队列中取出客户端, 交给工作线程 do_process, 如果工作线程满，则被阻塞，排队等待
            client_data = queue.get()
            client_socket = client_data[0]
            client_addr = client_data[1]
            print client_socket, " from ", client_addr

            if not client_socket:
                break
            thread_list.append(do_process(client_socket, client_addr))
            queue.task_done()

def do_process(client_socket, client_addr):
    while True:
        data = client_socket.recv(1024)
        print data 
        if data == "quit" or not data:
            print client_socket, " from ", client_addr, "quit!"
            break

        if data == "gedit":
            os.popen("/usr/bin/gedit")

        if data == "nautilus":
            os.popen("/usr/bin/nautilus")

        if data == "xterm":
            os.popen("/usr/bin/xterm")

        back_data = data+" finished!"
        client_socket.send(back_data)

    client_list.remove(client_socket)
    print "Remove ", client_socket, " Total: ", len(client_list)
    client_socket.close()

if __name__ == "__main__":
    NUM = 2 
    client_list = []
    queue = Queue.Queue()
    thread_list = []
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 50000))
    s.listen(1)

# 创建NUM个线程，如果有超个NUM个客户端连接，则阻塞, 排队等待, 线程池管理器, 用于创建并管理线程池 
    for thread_num in range(NUM):
        t = Mythread()
        t.setDaemon(1)
        t.start()

# 接收客户端的连接，将其放入队列, 获取排队的客户端
    while True:
        try:
            client_socket, client_addr = s.accept()
        except:
            print client_socket, " error"
            os._exit(0)

        if client_socket:
            client_list.append(client_socket)

        print "Client Total: ", len(client_list)
        if len(client_list) > 2:
            client_socket.send("waiting")

        queue.put((client_socket, client_addr))

    queue.join()

