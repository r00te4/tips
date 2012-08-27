#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		file_time.py
#     Desc:		time module function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-05-27 16:10:25
#     History:		
#=============================================================================
'''
import time
#time模块提供各种操作时间的函数
#说明：一般有两种表示时间的方式:
    #第一种是时间戳的方式(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的
    #第二种以数组的形式表示即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同
    #year    (four digits, e.g. 1998)
    #month   (1-12)
    #day     (1-31)
    #hours   (0-23)
    #minutes (0-59)
    #seconds (0-59)
    #weekday (0-6, Monday is 0)
    #Julian day (day in the year, 1-366)
    #DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时

#time() -" floating point number:返回当前时间的时间戳
print "time.time:", time.time()

#asctime([tuple])  将一个struct_time(默认为当时时间)，转换成字符串
print "time.asctime:", time.asctime()

#clock() 该函数有两个功能:
    #在第一次调用的时候，返回的是程序运行的实际时间；
    #以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
print "time.clock:", time.clock()

#sleep(seconds) :#可以通过调用time.sleep来挂起当前的进程,time.sleep接收一个浮点型参数，表示进程挂起的时间
time.sleep(1)

#ctime(seconds) :将一个时间戳(默认为当前时间)转换成一个时间字符串
print "time.ctime:", time.ctime(time.time())


#gmtime([seconds])  (tm_year, tm_mon, tm_day, tm_hour, tm_min,tm_sec, tm_wday, tm_yday, tm_isdst):
#将一个时间戳转换成一个UTC时区(0时区)的struct_time，如果seconds参数未输入，则以当前时间为转换标准
print "time.gmtime:", time.gmtime(time.time())

#time.localtime与time.gmtime非常类似，也返回一个struct_time对象，可以把它看作是gmtime()的本地化版本
print "time.localtime:", time.localtime(time.time())

#mktime(tuple) floating point number:
    #time.mktime执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数
print "time.mktime:", time.mktime(time.localtime())

#strftime(format[, tuple]):将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
#python中时间日期格式化符号：
#   %y 两位数的年份表示（00-99）
#   %Y 四位数的年份表示（000-9999）
#   %m 月份（01-12）
#   %d 月内中的一天（0-31）
#   %H 24小时制小时数（0-23）
#   %I 12小时制小时数（01-12）
#   %M 分钟数（00=59）
#   %S 秒（00-59）
#   %a 本地简化星期名称
#   %A 本地完整星期名称
#   %b 本地简化的月份名称
#   %B 本地完整的月份名称
#   %c 本地相应的日期表示和时间表示
#   %j 年内的一天（001-366）
#   %p 本地A.M.或P.M.的等价符
#   %U 一年中的星期数（00-53）星期天为星期的开始
#   %w 星期（0-6），星期天为星期的开始
#   %W 一年中的星期数（00-53）星期一为星期的开始
#   %x 本地相应的日期表示
#   %X 本地相应的时间表示
#   %Z 当前时区的名称
#   %% %号本身
print "time.strftime:", time.strftime('%Y-%m-%d %H:%M:%S')
print "time.strftime:", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())  # UTC时区

#strptime(string, format) struct_time:将时间字符串根据指定的格式化符转换成数组形式的时间
#2009-03-20 11:45:39  对应的格式化字符串为：%Y-%m-%d %H:%M:%S
#Sat Mar 28 22:24:24 2009 对应的格式化字符串为：%a %b %d %H:%M:%S %Y
print "time.strptime:", time.strptime('2009-06-23 15:30:53', '%Y-%m-%d %H:%M:%S')  

#python获取当前时间
#time.time() 获取当前时间戳
#time.localtime() 当前时间的struct_time形式
#time.ctime() 当前时间的字符串形式

#python格式化字符串
#格式化成2009-03-20 11:45:39形式：
    #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#格式化成Sat Mar 28 22:24:24 2009形式：
    #time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

#将格式字符串转换为时间戳
#a = "Sat Mar 28 22:24:24 2009"
#b = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
#print b
#1238250264.0
