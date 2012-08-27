#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_zip.py
#     Desc:		show zip module functions
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-25 13:32:00
#     History:		
#=============================================================================
'''

import os
import zipfile

# ----------------------------------------------
#首先需要明确两个概念：归档文件和压缩文件
    #归档文件是将一组文件或目录保存在一个文件
    #压缩文件也是将一组文件或目录保存一个文件中，并按照某种存储格式保存在磁盘上，所占磁盘空间比其中所有文件总和要少
    #因此，归档文件是没有经过压缩的，它所使用的磁盘空间仍等于其所有文件的总和, 用户可以将归档文件再进行压缩，使其容量更小

#gzip是Linux中最流行的压缩工具，具有很好的移植性，可在很多不同架构的系统中使用
#bzip2在性能上优于gzip，提供了最大限度的压缩比率
#如果用户需要经常在Linux和微软Windows间交换文件，建议使用zip
    #压缩工具        解压工具       文件扩展名
    #gzip            gunzip          .gz
    #bzip2           bunzip2         .bz2
    #zip             unzip           .zip


# ----------------------------------------------
# ZipFile模块用来做zip格式编码的压缩和解压缩的，由于是很常见的zip格式，所以这个模块使用频率也是比较高的
# ZipFile模块现在还不能处理分卷zip文件和带有注释的zip文件
# ZipFile里有两个非常重要的class, 分别是ZipFile和ZipInfo
    #ZipFile 是主要的类，用来创建和读取zip文件
    #ZipInfo 是存储的zip文件的每个文件的信息的


# -------------------创建zip文件---------------------------
#zipfile.ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=False)
    #mode:          'r'表示打开一个存在的只读ZIP文件; 'w'表示清空并打开一个只写的ZIP文件，或创建一个只写的ZIP文件；'a'表示打开一个ZIP文件，并添加内容。 
    #compression:   表示压缩格式，可选的压缩格式只有2个：zipfile.ZIP_STORE是默认的，表示不压缩； zipfile.ZIP_DEFLATED表示压缩
    #allowZip64:    为True时，表示支持64位的压缩，一般而言，在所压缩的文件大于2G时，会用到这个选项；默认情况下，该值为False，因为Unix系统不支持 

#zipfile.close()
    #写入的任何文件在关闭之前不会真正写入磁盘

#zipfile.write(self, filename, arcname=None, compress_type=None)
    #acrname:    是压缩文件中该文件的名字，默认情况下和filename一样 
    #compress_type:  是因为zip文件允许被压缩的文件可以有不同的压缩类型 

# zipfile.write()创建zip有点变态：
    #filename只能是某个具体的文件，不能是目录
    #创建的zip解压后，都是含有绝对路径的，但我只想解开到具体的某一层次目录怎么办？
    #这时，可以为write的第二个参数指定一个相对路径来替换完整的绝对路径
    #os.path.relpath(path[, start])  #从start开始计算相对路径
    #比如：
    #绝对路径为：abs_path = "/root/Desktop/hp_cert/2011HardwareDriverStatus-HP-11-04-13.xlsx"
    #相对路径为：rel_path = os.path.relpath(abs_path, os.path.dirname("/root/Desktop/")), 即得到："hp_cert/2011HardwareDriverStatus-HP-11-04-13.xlsx"
    #对应关系为："/root/Desktop/hp_cert/2011HardwareDriverStatus-HP-11-04-13.xlsx"   <=> "hp_cert/2011HardwareDriverStatus-HP-11-04-13.xlsx"
    #如果想对某个目录创建zip，可os.walk(dir)整个目录，得到完整的文件绝对路径后，再使用write来创建

z = zipfile.ZipFile("zipfile.zip", "w")
test_dir = "/root/Desktop/hp_cert/"
for root, dirs, names in os.walk(test_dir):
    for filename in names:
        abs_path = os.path.join(root, filename)
        rel_path = os.path.relpath(abs_path, os.path.dirname("/root/Desktop/"))
        z.write(abs_path, rel_path, compress_type=zipfile.ZIP_DEFLATED)

#zipfile.writestr( )支持将二进制数据直接写入到压缩文档
    #参数一： 指定一个存放数据的文件
    #参数二： 需要写入的数据
z.writestr('writestr.txt', 'Test zipfile.writestr() functions:\nSucessfully')


# -------------------操作zip文件---------------------------
#解压所有文件到指定目录: zipfile.extractall(self, path=None, members=None, pwd=None) 
    #path:   解压缩目录
    #member: 需要解压缩的文件名儿列表 
    #password:   当zip文件有密码时需要该选项 

#逐个解压文件到指定目录 zipfile.extract(self, member, path=None, pwd=None)
#for filename in z.namelist():
    #z.extract(filename, output_dir)

#zipfile.is_zipfile(filename) 判断一个文件是不是压缩文件 
#z.infolist()    获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
#z.namelist()    获取zip文档内所有文件的名称列表
#z.printdir()    打印压缩文件夹的信息 

#z.read(self, name, pwd=None)  读取zip文件中的某个文件，返回一个字符串

output_dir = "/root/Desktop/Python/example/file/kk"
z.extractall(output_dir)

string = z.read("writestr.txt")
print string


#ZipInfo.filename： 获取文件名称。
#ZipInfo.date_time： 获取文件最后修改时间。返回一个包含6个元素的元组：(年, 月, 日, 时, 分, 秒)
#ZipInfo.compress_type： 压缩类型。
#ZipInfo.comment： 文档说明。
#ZipInfo.extra： 扩展项数据。
#ZipInfo.create_system： 获取创建该zip文档的系统。
#ZipInfo.create_version： 获取 创建zip文档的PKZIP版本。
#ZipInfo.extract_version： 获取 解压zip文档所需的PKZIP版本。
#ZipInfo.reserved： 预留字段，当前实现总是返回0。
#ZipInfo.flag_bits： zip标志位。
#ZipInfo.volume： 文件头的卷标。
#ZipInfo.internal_attr： 内部属性。
#ZipInfo.external_attr： 外部属性。
#ZipInfo.header_offset： 文件头偏移位。
#ZipInfo.CRC： 未压缩文件的CRC-32。
#ZipInfo.compress_size： 获取压缩后的大小。
#ZipInfo.file_size： 获取未压缩的文件大小。

z_info = z.getinfo('hp_cert/AddOnScripts/validity-fpr')  
print 'filename:', z_info.filename  
print 'date_time:', z_info.date_time  
print 'compress_type:', z_info.compress_type  
print 'comment:', z_info.comment  
print 'extra:', z_info.extra  
print 'create_system:', z_info.create_system  
print 'create_version:', z_info.create_version  
print 'extract_version:', z_info.extract_version  
print 'extract_version:', z_info.reserved  
print 'flag_bits:', z_info.flag_bits  
print 'volume:', z_info.volume  
print 'internal_attr:', z_info.internal_attr  
print 'external_attr:', z_info.external_attr  
print 'header_offset:', z_info.header_offset  
print 'CRC:', z_info.CRC  
print 'compress_size:', z_info.compress_size  
print 'file_size:', z_info.file_size  

z.close()

#zip文件格式信息 
#一个 ZIP 文件由三个部分组成：压缩源文件数据区+压缩源文件目录区+压缩源文件目录结束标志 
#1)压缩源文件数据区 
#在这个数据区中每一个压缩的源文件/目录都是一条记录，记录的格式如下： [文件头+ 文件数据 + 数据描述符] 
#　　 a、文件头结构 
        #组成                    长度 
#　　 文件头标记                 4 bytes (0x04034b50) 
#　　 解压文件所需 pkware 版本   2 bytes 
#　　 全局方式位标记             2 bytes 
#　　 压缩方式                   2 bytes 
#　　 最后修改文件时间           2 bytes 
#　　 最后修改文件日期           2 bytes 
#　　 CRC-32校验                 4 bytes 
#　　 压缩后尺寸                 4 bytes 
#　　 未压缩尺寸                 4 bytes 
#　　 文件名长度                 2 bytes 
#　　 扩展记录长度               2 bytes 
#　　 文件名                     (不定长度)
#　　 扩展字段                   (不定长度)
#　　 
#　　 b、文件数据 
#　　 
#　　 c、数据描述符 
#　　    组成                    长度 
#　　 CRC-32校验                 4 bytes 
#　　 压缩后尺寸                 4 bytes 
#　　 未压缩尺寸                 4 bytes 
#　　 
#2)压缩源文件目录区 
#　　 在这个数据区中每一条纪录对应在压缩源文件数据区中的一条数据 
#　　 组成                       长度 
#　　 目录中文件文件头标记       4 bytes (0x02014b50) 
#　　 压缩使用的pkware 版本      2 bytes 
#　　 解压文件所需 pkware 版本   2 bytes 
#　　 全局方式位标记             2 bytes 
#　　 压缩方式                   2 bytes 
#　　 最后修改文件时间           2 bytes 
#　　 最后修改文件日期           2 bytes 
#　　 ＣＲＣ－３２校验           4 bytes 
#　　 压缩后尺寸                 4 bytes 
#　　 未压缩尺寸                 4 bytes 
#　　 文件名长度                 2 bytes 
#　　 扩展字段长度               2 bytes 
#　　 文件注释长度               2 bytes 
#　　 磁盘开始号                 2 bytes 
#　　 内部文件属性               2 bytes 
#　　 外部文件属性               4 bytes 
#　　 局部头部偏移量             4 bytes 
#　　 文件名                     (不定长度)
#　　 扩展字段                   (不定长度) 
#　　 文件注释                   (不定长度) 
#　　 
#3)压缩源文件目录结束标志 
#　　 组成                       长度 
#　　 目录结束标记               4 bytes (0x02014b50) 
#　　 当前磁盘编号               2 bytes 
#　　 目录区开始磁盘编号         2 bytes 
#　　 本磁盘上纪录总数           2 bytes 
#　　 目录区中纪录总数           2 bytes 
#　　 目录区尺寸大小             4 bytes 
#　　 目录区对第一张磁盘的偏移量 4 bytes 
#　　 ZIP 文件注释长度           2 bytes 
#　　 ZIP 文件注释               (不定长度)
