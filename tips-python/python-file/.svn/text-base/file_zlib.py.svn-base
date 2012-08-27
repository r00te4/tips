#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_zlib.py
#     Desc:		zlib module functions
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-25 17:56:45
#     History:		
#=============================================================================
'''
#zlib 是一个通用目的压缩/解压功能库。它的所有代码都是线程安全的
#zlib 的压缩核心算法和 gzip、Zip (PKZip, WinZip) 相同，称为 deflate
#zlib 用在内存数据，通信信道数据的压缩。zlib 有 2B 的头部标识（比 gzip 的小），和 4B 用于解压后的校验的尾部
#gzip 用在文件的压缩，比 zlib 有更大的头部以保存目录信息，并使用不同的校验算法，比 zlib 慢些


#zlib.compress(string[, level])
#zlib.decompress(string[, wbits[, bufsize]])

#zlib.compress用于压缩流数据, 
    #参数string指定了要压缩的数据流，
    #参数level指定了压缩的级别，它的取值范围是1到9。压缩速度与压缩率成反比，1表示压缩速度最快，而压缩率最低，而9则表示压缩速度最慢但压缩率最高
    
#zlib.decompress用于解压数据
    #参数 string指定了需要解压的数据
    #wbits和bufsize分别用于设置系统缓冲区大小(window buffer )与输出缓冲区大小(output buffer)

import zlib
import urllib2

fp = urllib2.urlopen("http://www.google.com")
str = fp.read()
fp.close()

str1 = zlib.compress(str, zlib.Z_BEST_COMPRESSION)
str2 = zlib.decompress(str1)

print len(str)
print len(str1)
print len(str2)


#现在要压缩一个非常大的数据文件（上百M）:
#使用zlib.compress来压缩的话，必须先一次性将文件里的数据读到内存里，然后将数据进行压缩,这样势必会占用太多的内存
#如果使用对象com_obj = zlib.compressobj()来进行压缩，那么没有必要一次性读取文件的所有数据:
#可以先读一部分数据到内存里进行压缩，压缩完后写入文件，然后再读其他部分的数据压缩，如此循环重复，直到压缩完整个文件
#另外，对于超大数据，一般原则都是先分块，再处理
#com_obj = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
#str_obj = com_obj.compress(data)
#str_obj += com_obj.flush()
#print '压缩后：', len(str_obj)

#decom_obj = zlib.decompressobj()
#str_obj1 = decom_obj.decompress(str_obj)
#str_obj1 += decom_obj.flush()
#print '解压后：', len(str_obj1)

def compress_fun(com_file, dst_file):
    com_f = open(com_file, "rb")
    dst_f = open(dst_file, "wb")
    com_obj = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
    data = com_f.read(1024) 
    while data:
        dst_f.write(com_obj.compress(data))
        data = com_f.read(1024)
    dst_f.write(com_obj.flush())

def decompress_fun(dst_file, com_file):
    dst_file = open(dst_file, "rb")
    com_file = open(com_file, "wb")
    dst_obj = zlib.decompressobj()
    data = dst_file.read(1024)
    while data:
        com_file.write(dst_obj.decompress(data))
        data = dst_file.read(1024)
    com_file.write(dst_obj.flush())

org_file = "os.example.py"
dst_file = "dst.dat"
bak_file = "os.example.bak"

compress_fun(org_file, dst_file)
decompress_fun(dst_file, bak_file)

