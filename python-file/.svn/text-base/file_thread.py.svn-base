#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_tread.py
#     Desc:		block file and use tread function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-05 11:08:44
#     History:		
#=============================================================================
'''

import threading
import Queue
import re
import os
import datetime
import time

# 一般我们对普通处理文件进行处理时都会采用下面的代码
# for lines in open(logfile).readlines():
#        doSomeProcess().....#具体的处理内容

# 而对于百M级别甚至G级别的文件，这时候再采用上面的方式显然不合适，有几种解决方式:
#    1.多线程(Multiple Thread)的处理方式
#    2.多进程(Multiple Processes)的处理方式
#    3.存储器映像(Memory Mapping)的处理方式
         
#多线程首先就是要把单个文件区块化，比如说200M的文件区块化为200个1M的区块，针对每个区块进行具体的处理可通过队列进行并行处理


# 文件分块化：
# 传递两个参数：文件名，分块的大小
# blocklist_start 列表记录每一个块的开头
# blocklist_end 列表记录每一个块的结束
# file.readlines(blocksize) 读取分块大小, 确保区块在换行符后结束，所以严格上来说并非每个区块都是很严格的blocksize
# if not lines or file.tell() == filesize 文件分块结束
# zip(blocklist_start, blocklist_end) 合并分块标记，得到一组分块的定位位置

#def getblocks(logfile, blocksize):
    #filesize = os.stat(logfile).st_size
    #file = open(logfile, 'rU')
    #blocklist_start = []
    #blocklist_end = []
    #while True:
        #pos = file.tell()
        #blocklist_start.append(pos)
        #lines = file.readlines(blocksize)
        #blocklist_end.append(file.tell())
        #if not lines or file.tell() == filesize:
            #break
    #return zip(blocklist_start, blocklist_end)
                      

# 指定NUM，将文件分成NUM份，这样分出来的文件不会考虑换行符是否结束，严格划分，实用于二进制
def getblocks(logfile, num):
    filesize = os.stat(logfile).st_size
    block = filesize/num
    blocklist_start=[]
    blocklist_end = []
    for i in range(0, num):
        blocklist_start.append(block*i)
        
    for i in range(1, num):
        blocklist_end.append(block*i)
    blocklist_end.append(filesize)
    return zip(blocklist_start, blocklist_end)


# 线程调用函数, 此处分将原文件分割成几部分，每一个子文件用block_end来命名
# http://www.oschina.net/code/snippet_16840_1998, 参考文件分割合并
def doProcess(file, block_start, block_end, partname):
    print file, block_start, block_end, partname
    f = open(file, 'rb')

    while True:
        f.seek(block_start)
        lines = f.read(block_end-block_start) 
        open(partname, 'wb').write(lines)
        if f.tell() == block_end:
            break


# 自定义线程类，通过继承 threading.Thread 的方式创建
class Mythread(threading.Thread):
    def run(self):
        print "The Thread name is: ", self.getName()
        while True:
            filename_block = queue.get()
            filename = filename_block[0]

            blocksize = filename_block[1]
            blocksize_start = blocksize[0]
            blocksize_end = blocksize[1]

            partname = filename_block[2]

            if filename_block is None:
                break
            thread_list.append(doProcess(filename, blocksize_start, blocksize_end, partname))
            queue.task_done()


# 程序主体部分
if __name__=="__main__":
    #LOGFILE = "one_char.py"
    #LOGFILE = "libX11.txt"
    LOGFILE = "/root/Desktop/Certification-Test/add-on-0.9.5.iso"
    BLOCKSIZE = 512*512
    NUM = 5

    queue = Queue.Queue()
    #filesplit = getblocks(LOGFILE, BLOCKSIZE)
    filesplit = getblocks(LOGFILE, NUM)
    thread_list =[]

    #for thread_num in range(len(filesplit)):
    for thread_num in range(NUM):
        t = Mythread()
        t.setDaemon(1)
        t.start()

    partnum = 0
    for pos in filesplit:
        print pos
        partnum = partnum+1
        partname = "part_%04d" %partnum
        queue.put((LOGFILE, pos, partname))

# join() 保持阻塞状态，直到处理了队列中的所有项目为止
    queue.join()
 

# 创建自己的线程类，必要时重写threading.Thread类的方法，线程的控制可以由自己定制
# threading.Thread类的使用：
    #1，在自己的线程类的__init__里调用threading.Thread.__init__(self, name = threadname)
    #2，run()，通常需要重写，编写代码实现做需要的功能
    #3，getName()，获得线程对象名称
    #4，setName()，设置线程对象名称
    #5，start()，启动线程
    #6，jion([timeout])，等待另一线程结束后再运行
    #7，setDaemon(bool)，设置子线程是否随主线程一起结束，必须在start()之前调用, 默认为False。
    #8，isDaemon()，判断线程是否随主线程一起结束
    #9，isAlive()，检查线程是否在运行中

# 在 Python 中使用线程时，队列模式是一种很常见的并且推荐使用的方式,具体工作步骤描述如下：
    #1. 创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充: queue.put()
    #2. 将经过填充数据的实例传递给线程类，然后使用queue.get()获取数据
    #3. 生成守护线程池
    #4. 每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作
    #5. 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号
    #6. 对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序

