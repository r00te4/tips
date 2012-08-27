#! /usr/bin/python
#!coding=utf8
'''
#=============================================================================
#     FileName:		dict_fun.py
#     Desc:		This program will show dict function
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-26 13:14:41
#     History:		
#=============================================================================
'''
# 字典中的键/值对是没有顺序的, 如果想要一个特定的顺序，那么你应该在使用前自己对它们排序
# 只能使用不可变的对象（比如字符串）来作为字典的键，但是可以用不可变或可变的对象作为字典的值
# 键必须是唯一的
# 键/值对用冒号分割，而各个对用逗号分割，所有这些都包括在花括号中

dict_key_value = {"redflag":"qomo", "novell":"suse", "ylmf":"linux"}

# 字典的长度
print len(dict_key_value)

# 增加一对键值, 两种方法
# setdefault(key,default=None), 如果dict中有key，则返回key值，如果没有找到key，则在dict中加上该key，值由default参数给出，默认None
dict_key_value["redhat"] = "fedora"
dict_key_value.setdefault("ub","ubuntu")

# 替换一对键值
dict_key_value["novell"] = "opensuse"

# 删除一对键值, 如果key不在字典中，则返回异常
del dict_key_value['ub']

# pop() 删除一对键值,并返回该键对应的值, 如果key不在字典中，则返回异常
print dict_key_value.pop("redhat")

# popitem() 删除任意键－值对，不确定那一对被删除，返回该键－值对，如字典为空，则产生异常
print dict_key_value.popitem()

# 打印整个字典元素
print dict_key_value, '\n'

# 取某个键的值
print dict_key_value["redflag"], '\n'
print dict_key_value.get("novell")

# 取某个键值，如果不存在或为空，则返回0
if dict_key_value.get("novells"):
    print dict_key_value.get("novell")
else:
    print "No find this key"

# 判断字典里是否有某个键存在，如果存在的话返回True，不存在的话返回False
if dict_key_value.has_key("redflag"):
    print "this key exist"
else:
    print "not exist"

# 遍历所有键的值 dict.values()
for value in dict_key_value.values():
    print value

print "\n"
# 遍历所有键的名 dict.keys()
for key in dict_key_value.keys():
    print key

print "\n"
# 遍历所有的键和值 dict.items()
for key, value in dict_key_value.items():
    print "key is: %s" %key
    print "value is: %s" %value

# update(dict2), 把dict2的元素加入到dict中去，键字重复时会覆盖dict中的键值

# 清除所有键值
dict_key_value.clear()
print dict_key_value

print "\n"


# iteritems, itervalues, iterkeys
# items和iteritems方法:
# items方法是以列表方式返回字典中所有项，这些列表项中的每一项都来自于（键，值），但是项在返回时并没有特殊的顺序（为什么？因为字典无序！！)
# 而iteritems方法与items类似，但其返回一个迭代器对象，而不是列表
dict_iter = {"aa":"11", "bb":"22", "cc":"33"}
for iter_value in dict_iter.itervalues():
    print iter_value

for iter_key in dict_iter.iterkeys():
    print iter_key

for iter_key, iter_value in dict_iter.iteritems():
    print iter_key
    print iter_value


# 将一个列表元素交替的作为键和值来创建字典, zip()及切片的用法
Name_List = ["hsun", "030802", "forrest", "924890", "hongsun", "134324"]
print Name_List[1::2]
def DictfromList(keysAndValues):
    return dict(zip(keysAndValues[::2], keysAndValues[1::2]))

print DictfromList(Name_List)


# 根据一个字典的某些键，创建一个子字典, 不删除原字典数据, dict.get(k, default )
def sub_dict(somedict, somekeys, default=None):
    list_keys = [(k, somedict.get(k, default)) for k in somekeys]
    return dict(list_keys) 

d = {"1":"a", "2":"b", "3":"c"}
sub = ("2", "3","4")
print sub_dict(d, sub)
print sub_dict(d, sub, "d")
print d, '\n'


# 根据一个字典的某些键，创建一个子字典, 删除原字典中的子字典数据, dict.pop(k, default)
def sub_dict_remove(somedict, somekeys, default=None):
    list_keys = [(k, somedict.pop(k, default)) for k in somekeys]
    return dict(list_keys)

d = {"aa":"11", "bb":"22", "ab":"33"}
sub = ["aa", "ab"]
print sub_dict_remove(d, sub)
print d


# 反转一个字典，因为字典本身是无序的，这里说的反转一个字典，是指将字典的原先的键值调换，键:值 <=> 值:键
# 虽说键是唯一的，但不代表值也是唯一，如果这么一反转，那么对于那些值是相同的情况，就不太适用，使用前，反转前，需要先根据需求作一下过滤
d = {"aa":"11", "bb":"22", "ab":"33", "cc":"22"}
print d

def invert_dict(somedict):
    new_list = [(v,k) for k,v in somedict.iteritems()]
    #new_list =[(v,k) for k,v in somedict.items()]
    return dict(new_list)

def invert_dict_zip(somedict):
    new_list = zip(somedict.itervalues(), somedict.iterkeys())
    return dict(new_list)

from itertools import izip
def invert_dict_izip(somedict):
    new_list = izip(somedict.itervalues(), somedict.iterkeys())
    return dict(new_list)

print invert_dict(d)
print invert_dict_zip(d)
print invert_dict_izip(d)



# 一键多值, 正常情况下，字典是一对一映射的，下面方法可实现一对多的映射
d1 = {"hello":"world"}
d1.setdefault("aa",["11", "22", "33"]).append("22")
print d1["aa"]
print d1

# set()是内建类set的构造函数, 返回一个集合对象
# 函数的参数可以是列表，或者元祖，反正是一串儿的都可以
# 集合的特点是其元素不可以重复, 把一堆东西放到一起，类似列表，不同的地方是内容不重复，而且也没有次序
# aset = set([1, 2, 3, 2, 4, 6]) # 去掉重复内容，所以是 1,2,3,4,6
# 集合也是可以变成列表的，利用 list() 函数:  alist = list(aset) # 内容 [1,2,3,4,6]
d2 = {"suse":"linux"}
d2.setdefault("redflag", set(["qomo", "DT6.0"])).add("DT6.0")
print d2["redflag"]
print d2



# 字典的交集或并集
d1 = {"aa":"11", "bb":"22", "cc":"33", "dd":"44"}
d2 = {"ab":"12", "bb":"23", "ac":"33", "dd":"44"}

print list(d1)
print tuple(d1)
print dict(d1)
print set(d1)
print set(d1) | set(d2)  # 取并集
print set(d1) & set(d2)  # 取交集


# -------------------------------------------------------------
# 排序 sort(): L.sort(cmp=None, key=None, reverse=False)
# cmp和key一般使用lambda
list_s = ["joke", "zero", "about", "Kiss"]

# 使用sort()对列表排序，默认字母升序，区分大小写，大写优先排列
list_s.sort()
print list_s

# 使用 cmp 方法来忽略字母大小写;  如果使用sorted(string_list, key=str.lower),同样可以忽略大小写
list_s.sort(cmp = lambda x,y: cmp(x.lower(), y.lower()))
print list_s

# 使用 reverse = True 来降序排列
list_s.sort(cmp = lambda x,y: cmp(x.lower(), y.lower()), reverse = True)
print list_s


# 对于key 的使用, 考虑这样一个类Person, 有两个属性，Person.age, Person.gender:
# key的作用是可以指定按年龄还是按性别排序
# cmp的作用是可以指定排序的标准（例如以年龄排序时升序还是降序，以性别排序时何种性别在前）
name = ["Tom", "John", "Forrest", "Robert"]
age = [34, 24, 45, 32]
gender = ["man", "woman", "man", "woman"]

# 使用zip合并为一个同元组构成的列表
list_zip = zip(name, age, gender)

# sort默认按name排序，key = lambda x: x[0], 区分大小写
list_zip.sort()
print list_zip

# 按age来排序
list_zip.sort(key = lambda x: x[1])
print list_zip

# 按gender来排序
list_zip.sort(key = lambda x: x[2])
list_zip.sort(key = lambda x: x[2], reverse = True)
print list_zip


#----------------------------------------------------
# sorted(): sorted(iterable, cmp=None, key=None, reverse=False) --" new sorted list
# sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表。
# 对于一个字典，只要使用dict去生成，其print的结果必然是无序的，所以一般使用sort或sorted来排序出一个元组列表

d={"Ok":1, "yes":3, "no":2}

# 对字典按键排序，用元组列表的形式返回
print sorted(d.iteritems(), key=lambda d: d[1])
print sorted(d.iteritems(), key=lambda d: d[0], cmp = lambda x,y: cmp(x.lower(), y.lower()) )   #忽略大小写

# 对字典按值排序，用元组列表的形式返回
print sorted(d.iteritems(), key=lambda d: d[1])

# sorted() 不像sort()只针对列表排序，还可对字符串，元组, 字典排序，因为只要字符参数形式是一个 iterable 即可
mystring = "53412dadad"
print sorted(mystring)

mytuple = (5,3,4,1,2)
print sorted(mytuple)

mylist = [5,3,4,1,2]
print sorted(mylist)

mydict = dict(a=3, c=5, b=1, d=4)
print sorted(mydict.items())

# 字符串，元组, 列表，相互转换, 切记不要在程序中使用与内建函数同名的函数名作为变量名！
print list(mystring)
print tuple(mystring)

print list(mytuple)
print tuple(mylist)

# 在一个列表中查找是否存在某个元素
def list_search(somelist, key):
    if key in somelist:
        return somelist.index(key)
    else:
        return "No found"

list_s = ["hello", "workd", "hongsun", 924, "linux"]
print list_search(list_s, "hongsun") 


# 找出两个列表中相同的元素
list1 = ["hi", "yes", "no", "suse", 99]
list2 = ["ho", "yes", "no", "linux", 99]
new_set = set(list1) & set(list2)
new_list = list(new_set)
print sorted(new_list)


#Python 3.0 有序字典: from collections import OrderedDict


# 最大堆和最小堆是二叉堆的两种形式
# 最大堆：根结点的键值是所有堆结点键值中最大者
# 最小堆：根结点的键值是所有堆结点键值中最小者

# 堆排序是在排序过程中，将向量中存储的数据看成一棵完全二叉树，利用完全二叉树中双亲结点和孩子结点之间的内在关系来选择关键字最小的记录，即待排序记录仍采用向量数组方式存储，并非采用树的存储结构，而仅仅是采用完全二叉树的顺序结构的特征进行分析而已

#Python中最广为熟知的container就是list和dict了. 但是对于特定的用途, 这二者未必是最高效的.比如判断容器中是否包括x(x in container):
#如果容器是list就需要O(n)的时间.而使用set的话这个就只需要O(1)的时间.

#集合(Set):
#   set是Python的built-in类型,对于membership testing,　removing duplicates 的操作非常高校(O(1)时间).
#   另外对集合操作也非常方便.如果对容器元素的顺序没有要求,set是非常好的选择对象

#栈(Stack, FILO):
#   栈的特点是先进后出(FILO).built-in的list用来实现栈非常合适.对于append和pop的实现非常高效.

#队列(Queue, FIFO):
#   队列的特点是先进先出(FIFO). list用来实现队列不够有效.collections.deque可以弥补这一缺点


#Python heapq 模块:
#   heapq实现了适用于Python列表的小顶堆排序算法.
#   大顶堆确保每个父元素都大于或等于他的任一个孩子元素. 而小顶堆则需要每个父元素都要小于或等于他的任一个孩子元素. Python的heapq模块实现的是小顶堆.
#   有两个基本的堆创建方式, 分别是heappush()和heapify().
#   heapq.heappush(), 堆中元素排序顺序是随着新元素的不断增加而不断更新的.
#   heapq.heapify(), 将列表原地转换为堆
#   heapq.heappop(), 删除堆中最小的元素
#   heapq.heapreplace(), 可以删除现有元素和用新的值替换已存元素

#   heap采用的是堆排序算法，sort采用的是归并排序算法
#   使用堆(heap)实现的优先队列(priority queue)可以在O(1)时间内得到队列中最小元素, O(logn)时间内插入或者删除一个元素
#   对一个列表增加元素，但是要保持序列顺序， 可使用 heapq 模块

import heapq

list_num = [58,132,43,54,34,23,432,62]
print list_num

# 基于原列表 构建 一个堆
heapq.heapify(list_num)
print list_num

# 从堆中找到最顶（最小）的元素，并从堆中删除
print heapq.heappop(list_num)
print list_num

# 向堆中添加元素，会自动重新构建堆
heapq.heappush(list_num, 55)
heapq.heappush(list_num, 79)
heapq.heappush(list_num, 15)
print list_num

# 堆排序
new_list = [heapq.heappop(list_num) for i in range(len(list_num))]
print new_list

