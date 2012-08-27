#! /usr/bin/pthyon
'''
#=============================================================================
#     FileName:		test.py
#     Desc:		    for test
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-07-14 16:44:48
#     History:		
#=============================================================================
'''

import os

filename = "/root/Desktop/Certification-Test/add-on-0.9.5.iso"

file = open(filename, "r+")
size = os.path.getsize(filename)

newfile = open("mmap.iso", "w+")
newfile.write(file.read())
newfile.close()


