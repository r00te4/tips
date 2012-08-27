#! /usr/bin/python
#=============================================================================
#     FileName:		getopt_arg.py
#     Desc:		getopt Using info
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-06 13:55:17
#     History:		
#=============================================================================

import getopt, sys

#opts,args=getopt.getopt(sys.argv[1:], 'hv:', ['help','version'])
opts,args = getopt.gnu_getopt(sys.argv[1:], 'hvf:', ['help','version','file='])

for a,o in opts:
    if a in ('-h', '--help'):
        print ''' This program will show getopt info:
        -h, --help:     show help info
        -v, --version:  show version info
        -f filename, --file=filename , --file filename: input a file name
        '''
    elif a in ('-v', '--version'):
        print 'The program version is: 0.0.1'
    elif a in ('-f', '--file'):
        print 'the file name is %s' %o
    else:
        print "Usage: %s -h --help" %sys.argv[0]
        sys.exit(2)


#print opts
#print args

