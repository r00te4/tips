#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_tar_bak.py
#     Desc:		show tarfile moudel function, tarball with gz or bz2
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-24 16:38:42
#     History:		
#=============================================================================
'''

import os
import tarfile

#创建tarball, gz or bz2
#指定需要备份的文件目录:bak_dir， 
#指定备份文件存放路径： tar_dir

#创建一个Tarfile对象: tar = tarfile.open(tarname, w:gz)
    #参数一： tarball的名称
    #参数二： 读或写，以及压缩方式, w, w:gz, w:bz2
#添加需要备份的目标到Tarfile对象: tar.add(file,arcname="" )
    #参数一： 需要备份的目录或文件
    #参数二： arcname=None,默认备份完整的目录路经; arcname=""，只备份目录路径下的内容
    
bak_dir ="/root/Desktop/Python/example"
tar_dir = "/root/Desktop/Python/example/file/"

def do_compression(bak_dir, tar_dir, compression="bz2"):
    tar_name = "part_"+ os.path.basename(bak_dir)+".tar"+"."+compression
    full_path = tar_dir+tar_name

    out = tarfile.open(full_path, "w:"+compression) 
    out.add(bak_dir, arcname="")
    out.close()

do_compression(bak_dir, tar_dir, compression="gz")


# 解开tarball
# 指定需要解开的Tarfile对象: tar = tarfile.open(tarname)
# 使用tar.extractall(path="", members=None)，全部解开
    #参数一： 指定解压后存放的路径
    #参数二： 可为None
# 使用tar.extract(members="file", path)
    #参数一： 提取指定的文件，可遍历tar.getnames()来得到所有的tarball文件
    #参数二： 指定解压后存放的路径

# tar.getnames(self): Return the members of the archive as a list of their names.
# tar.list(self, verbose=True):  If `verbose' is False, only the names of the members are printed. If it is True, an `ls -l'-like output is produced.
# tar.getmembers():  Return the members of the archive as a list of TarInfo objects


tar = tarfile.open("/root/Desktop/Python/example/file/part_example.tar.gz")
tar.extractall(path="/root/Desktop/Python/example/file/kk", members=None)
filenames = tar.getnames()
for item in filenames:
    if item == "file/os.example.py":
        tar.extract("file/os.example.py", path="/root/Desktop/Python/example/file/kk")

print tar.getnames()
print tar.list()
