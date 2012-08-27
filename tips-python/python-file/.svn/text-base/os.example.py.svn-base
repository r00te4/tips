#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		os.example.py
#     Desc:		show os module function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-23 16:04:06
#     History:		
#=============================================================================
'''
import os
import shutil
import time
import re
import sys

#创建文件：
#1) os.mknod("test.txt")        创建空文件
#2) open("test.txt",w)          直接打开一个文件，如果文件不存在则创建文件
if os.path.exists("test.txt"):
    print "this file is exist!"
else:
    print "this file is not exist, created!"
    os.mknod("test.txt")

#创建目录：
#os.mkdir("test")                   创建目录
#os.mkdir("test/multiple/")
#os.makedirs("test/multiple/levels")
if os.path.exists("test"):
    print "this dir is exist!"
else:
    print "this dir is not exist, created!"
    os.mkdir("test")

#判断目标
#os.path.exists("goal") 判断目标是否存在
#os.path.isabs()        指定路径是否为绝对路径
#os.path.isdir()        指定路径是否存在且为一个目录
#os.path.isfile()       指定路径是否存在且为一个文件
#os.path.islink()       指定路径是否存在且为一个符号链接
#os.path.ismount()      指定路径是否存在且为一个挂载点
#os.path.samefile()     两个路径名是否指向同个文件
if os.path.isfile("test.txt"):
    print "this is a file"
else:
    print "this is not a file"

if os.path.isdir("test"):
    print "this is a dir"
else:
    print "this is not a dir"
 

#重命名文件（目录）
#os.rename("oldname","newname")       文件或目录都是使用这条命令
os.rename("test.txt", "new.txt")
os.rename("test", "newdir")


#修改文件权限
#os.chmod(path, mode)
#os.chown(path, uid, gid)
#os.umask(new_mask), 默认情况下的umask值是022(可以用umask命令查看），此时建立的文件默认权限是644，建立的目录的默认权限是755
os.chmod("new.txt", 777)
os.chown("new.txt", 1000, 100) 


#删除文件和空目录, removedirs,rmdir 只能删除空目录
#os.remove("file")
#os.removedirs("dir")
#os.rmdir("dir")
#shutil.rmtree("dir")    空目录、有内容的目录都可以删
os.remove("new.txt")
shutil.rmtree("newdir")


#复制文件：
#shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
#shutil.copy("oldfile","newfile")            oldfile只能是文件，newfile可以是文件，也可以是目标目录


#复制文件夹：
#shutil.copytree("olddir","newdir")        olddir和newdir都只能是目录，且newdir必须不存在


#移动文件（目录）
#shutil.move("oldpos","newpos")   


#转换目录路径
#os.chdir("path") 


#处理文件属性
#os.path.getsiz(fname)      filename的大小
#os.path.getatime(fname)    filename的最后访问时间
#os.path.getctime(fname)    filename的创建时间
#os.path.getmtime(fname)    filename的最后修改时间
#时间以秒为单位，并且从1970年1月1日开始算起
print os.path.getsize("os.example.py")
print os.path.getatime("os.example.py")
print os.path.getctime("os.example.py")
print os.path.getmtime("os.example.py")
print time.localtime(os.path.getatime("/root/bak/"))
print time.localtime(os.path.getctime("/root/bak/"))
print time.localtime(os.path.getmtime("/root/bak/"))


#stat 函数可以用来获取一个存在文件的信息, 它返回一个类元组对象(stat_result对象, 包含 10 个元素), 依次是:
#st_mode    文件权限模式
#st_ino     文件对应i-node节点号
#st_dev     文件对应设备号
#st_nlink   文件上硬连接的个数
#st_uid     文件所有者 UID)
#st_gid     文件所有者对应的组 GID
#st_size    文件字节数)
#st_atime   文件最后被访问的时间
#st_ctime   文件状态（属性）改变时间
#st_mtime   文件内容最后被修改的时间
#返回对象中有些属性在非 Unix 平台下是无意义的, 比如 (st_inode , st_dev)为 Unix 下的为每个文件提供了唯一标识, 但在其他平台可能为任意无意义数据
#可以使用 chmod 和 utime 函数修改文件的权限模式和时间属性
file_stat=os.stat("os.example.py")
print file_stat.st_mode
print file_stat.st_ino
print file_stat.st_dev
print file_stat.st_nlink
print file_stat.st_uid
print file_stat.st_gid

print file_stat.st_size
print file_stat.st_atime
print file_stat.st_ctime
print file_stat.st_mtime

print oct(file_stat.st_mode) #把整数x变成八进制表示的字符串
print time.ctime(file_stat.st_atime)
print time.ctime(file_stat.st_ctime)
print time.ctime(file_stat.st_mtime)


#分解路径名
#os.path.basename(file_path)    返回path的目录路径
#os.path.dirname(file_path)     返回path的文件名称
#os.path.split(file_path)       分割文件名与目录
#os.path.splitext(file_path)    分割文件名与扩展名
#os.path.join(path, name)       连接目录与文件名或目录
file_path = "/root/Desktop/Python/example/sys_os_path/os.example.py"
print os.path.basename(file_path)
print os.path.dirname(file_path)
print os.path.split(file_path)
print os.path.splitext(file_path)

newpath= os.path.join("/root/", "example.py")
print newpath


#遍历目录树
#os.walk() 该函数返回一个元组，该元组有3个元素:dirpath, dirnames, filenames
#dirpath   is a string, the path to the directory
#dirnames  is a list of the names of the subdirectories in dirpath (excluding '.' and '..')
#filenames is a list of the names of the non-directory files in dirpath 
for root, dirs, files in os.walk("/root/Desktop/Python/"):
    for filespath in files:
        print os.path.join(root, filespath)
#如果是windows目录，路径名中含有\, 可以使用os.sep 来代替, 如：os.walk('c:'+os.sep+'ant')，表示c:\ant


#os.path.walk函数被调用时需要指定目录的根、一个函数对象和可选的数据项，它将遍历根目录及以下的目录树
#函数声明：walk(top,func,arg)
#参数top表示需要遍历的目录树的路径
#参数func表示回调函数，对遍历路径进行处理.所谓回调函数，是作为某个函数的参数使用，当某个时间触发时，程序将调用定义好的回调函数处理某个任务.回调函数必须提供3个参数：
    #第1个参数为walk()的参数tag
    #第2个参数表示目录列表
    #第3个参数表示文件列表
#参数arg是传递给回调参数func的元组.回调函数的一个参数必须是arg，为回调函数提供处理参数.参数arg可以为空

def lister(dummy, dirname, filesindir):
    for fname in filesindir:
        print os.path.join(dirname, fname) 

os.path.walk('/root/Desktop/Python/', lister, None)

#os.path.walk()与os.walk()产生的文件名列表并不相同
#os.path.walk()产生目录树下的目录路径和文件路径
#os.walk()只产生文件路径


#改变工作目录，
#os.listdir(dirname)：列出dirname下的目录和文件
#os.getcwd() 获得当前工作目录
#os.curdir   返回当前目录（'.')
#os.chdir(dirname):改变工作目录到dirname
os.chdir("/root/Desktop/Python/example/")
print os.listdir(".")
print os.getcwd()
print os.curdir


#Python调用系统命令或者脚本
#使用 os.system() 调用系统命令 , 程序中无法获得到输出和返回值
os.system('ls -l /proc/cpuinfo')
#os.popen('/usr/bin/gedit &')


#使用 os.popen() 调用系统命令, 程序中可以获得命令输出，但是不能得到执行的返回值
out = os.popen("ls -lah")
print out.read()
#os.popen("/usr/bin/gedit &")


#os.name:返回当前操作系统名称（'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'）
#os.sep（文件路径名的分隔符，windows中是 \ ）
#os.extsep（文件扩展名分隔符，windows中是 . ）
#os.pathsep（指定不同目录，分隔符，windows中是 ; ）
#os.linesep（换行分隔符，windows中是 \r\n ）
print os.name
print os.sep
print os.extsep
print os.pathsep
print os.linesep


#----------------------遍历指定目录的文件，列出文件名含有某字符的文件----------
filedir = "/root/Desktop/Python/example"
keywords = "txt"
for root, dirs, names in os.walk(filedir):
    for filename in names:
        filename_split = os.path.splitext(filename)
        if filename_split[1] == ".py":
            print filename
#        if keywords in filename:
            #print os.path.join(root, filename)


#----------------------遍历指定目录的文件，列出含有某个内容的文件---------------
key = sys.argv[1]
for root, dirs, names in os.walk(filedir):
    for filename in names:
        tempfile = open(os.path.join(root, filename), "rb")
        for lines in tempfile.readlines():
            if re.search(key, lines, re.I):
                print lines



#路径问题
#os.path.abspath(path) #返回绝对路径
#os.path.basename(path) #返回文件名
#os.path.dirname(path) #返回文件路径
#os.path.realpath(path)  #返回path的真实路径
#os.path.relpath(path[, start])  #从start开始计算相对路径
