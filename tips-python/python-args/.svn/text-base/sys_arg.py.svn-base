#! /usr/bin/python
#=============================================================================
#     FileName:		sys_arg.py
#     Desc:		This program will be create for sys.argv using
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-01 15:39:55
#     History:		
#=============================================================================

import sys

if len(sys.argv)<2:
    print "Usage: %s arg1" %sys.argv[0]
    sys.exit()

# str.startswith() or str.endswith()
# sys.argv[1][2:]

if sys.argv[1].startswith("--"):
    print sys.argv[1][:2]
    print sys.argv[1][-2:]
    option=sys.argv[1][2:]
    if option=="version":
        print "The Version is: 0.0.1"
    elif option=="help":
        print '''This progrom will show the sys.argv using info:
        --help:     show help info
        --version:  show vresion info
        '''
    else:
        print "Unknow argv, error"
