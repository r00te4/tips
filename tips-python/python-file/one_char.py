#! /usr/bin/python
#coding=utf8
#=============================================================================
#     FileName:		one_char.py
#     Desc:		deal with one char from a long string
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-11 11:00:56
#     History:		
#=============================================================================
from __future__ import division
import sys
import re
import string
import locale
import struct
import os 
import itertools


# 每次获取一个字符，使用list内建函数，可将字符串分割成一个字符列表
list_char_a = list("hello world")
print list_char_a 

# 也可以使用for循环字符串，每次获取一个字符
for list_char_b in "Suse Linux": 
    print list_char_b


#========================字符与字符值转换=======================
# 把一个字符转化成ASCII码 
print ord('a')
print ord('b')

# 把ASCII转化成一个字符，ASCII最大码值255,注意chr()和repr(chr())的细小差别
print chr(97)
print chr(255)
print repr(chr(125))

# 把Unicode字符串转化成Unicode 码值；ord接收一个长度为1的Unicode字符串作为参数， 返回一个Unicode码值，最大到65535
print ord(u'\u2020')
print ord(u'\u9099')

# 把Unicode码值转化成Unicode 字符串；repr 结合内建函数unichr，可将一个数字的Unicode码值，转化成一个长度为1的Unicode字符串
print repr(unichr(1024))
print repr(unichr(65535))

# 把一个字符串转化成一系列 字符的值 的列表，使用map和ord
print map(ord,"hello, forrest")

# 把一系列 字符的值 转化成一个字符串，使用 .join, map, chr, 注意.join的用法
print ''.join(map(chr, range(97,105)))



#==========================测试一个对象是否是类字符串=====================
# 利用内建isinstance 和 basestring 来验证对象是否是字符串或Unicode, basestring是str和Unicode共同的基类;
# 但是对于Python中的UserString模块提供的UserString类的实例，完全无能为力
def isAString(anobj):
    return isinstance(anobj, basestring)

check_string=(u'\u2345')

if isAString(check_string):
    print "this is a string"
else:
    print "this is not a string"

# UserString 对象是非常明显的类字符串对象，只不过它不是从basestring派生的；
# 如果想支持这种类型，可以检查一个对象的行为是否真的像字符串一样
def isStringLike(anobj):
    try: anobj + ''
    except: return False
    else: return True

check_usersring = "Novell" 
if isStringLike(check_usersring):
    print "this is true"
else:
    print "this is false"


#==================================字符串对齐 .ljust(), .rjust(), .center() =================
# 实现字符串左对齐，右对齐，居中对齐，使用 .ljust(), .rjust(), .center()
# 每个方法都需要一个参数，指出生成字符串的宽度，默认使用空格补齐，但2.4版本以后，可以给这些方法第二个参数，来指定填充的字符
print "hello".ljust(10, '+')
print "hello".rjust(10, '+')
print "hello".center(10,'+')


char_just="hongsun"
print char_just.center(80,'+')


# ================================去除字符串两端的空格 .lstrip(), rstrip(), .strip()======================================
print '    redflag    linux '.lstrip()
print '    redflag    linux '.rstrip()
print '     redflag    linux '.strip()
print 'xxyxyxxyx hello worxydxyyyyxxxx'.strip('xy')  # 去除开头,结尾是x或y的字符



# ================================合并字符串.join(), %, + ==================================
# 使用 .join
char_list = ["hello", "world", "novell", "suse"]
print ''.join(char_list)

# 使用格式化操作符 %
small1 = "suse"
small2 = "novell"
small3 = "beijing"
largestring = '%s, this is %s, welcome %s' %(small1, small2, small3)
print largestring

# 使用连接符 ＋
largestring = small1+' '+small2+' '+small3
print largestring


# =============================逐字符反转字符串 或 逐词反转字符串列表===================
# 字符串无法改变，所以，反转一个字符串，需要创建一个拷贝；
# 最简单的方法就是使用一个步长为 -1 的切片方法
astring = "hongsun"
revchars =  astring[::-1]
print revchars

# 按单词来反转字符串，首先需要创建一个单词列表，将这个列表反转，最后在用.join将其合并, .join操作要使用原先的分隔符
astring = "hello,world,hong,sun,novell,linux,beijing"
print astring

revwords1 = astring.split(',')
revwords1.reverse()
revwords1 = ','.join(revwords1)
print revwords1

# 如果想逐词反转，但又不想改变原先的分隔符，可以用正则表达式来分隔原字符串, 这样最后的.join操作要使用空字符串，因为原先的分隔符也已经保存在revwords中了
revwords2 = re.split(r'(,+)', astring)
revwords2.reverse()
revwords2 = ''.join(revwords2)
print revwords2


# =====================================检查字符串中是否出现了某字符集合中的字符==================
# 给定一个特定的字符集合seq， 现在有一个字符串aset，需要检查这个字符串aset中的字符是否出现在那个给定的字符集合中
# 如果单纯的判断一个字符集合中是否含有某个字符或串，直接可以用 if aset in seq:
def containsAny(seq, aset):
    for c in seq:
        if c in aset:
            return True
    return False

seq = ["beijing"," hongsun","redflag","linux","qomo","suse","novell"]
aset = "s"
if containsAny(seq, aset):
    print "in seq list"
else:
    print "no in seq list"



# ===============================过滤字符串中指定的字符 maketrans and translate===================
s = "abcdefg-1234567"
table = string.maketrans('','')         # 指定一一对应的映射，此处没有映射对，实际上就是按原始字符保留,不作任何替换

print s.translate(table)                # 根据maketrans的映射 来替换字符
print s.translate(table, "abc")         # 先删除指定的abc字符, 然后再根据 table映射来替换 
print s.translate(table, "abc123")      
print s.translate(table, "abc-567")

table = string.maketrans('abc145', 'ABCabc')    # maketrans(intab, outtab)中两个字符串参数长度必须一样，因为是字符一对一的映射
print s.translate(table)                        # 根据maketrans的映射来替换字符
print s.translate(table, "abc")                 # 先删除指定的abc字符, 然后再根据 table映射来替换



# =================================判断文本文件或二进制文件===========================

ch =  ''.join(map(unichr, xrange(0x4e00, 0x9fa6)))  # 将unicode码值转换成unicode字符
zh = ch.encode('utf8')                              # 将unicode字符使用utf8编码
print ch.__class__
print zh.__class__

#kk = ''.join(map(unichr, xrange(0x0000,0xFFFF))) 
#print kk

text_characters = "".join(map(chr, range(32, 127))) + zh + "\n\r\t\b"
_null_trans = string.maketrans("", "")

def istextfile(filename, blocksize = 1024):
        return istext(open(filename).read(blocksize))

def istext(s):
    print s
    if "\0" in s:
        return False
    if not s:
        return True
    t = s.translate(_null_trans, text_characters)
    print "-----------------------------------------------------------"
    print t
    print len(t)/len(s)
    return len(t)/len(s) <= 0.30 

filename = "/root/Desktop/test-data/Bluetooth-setting.png"
#filename = "/root/Desktop/test-data/test.java"

if istextfile(filename, blocksize = 1024):
    print "this is text file"
else:
    print "this is banary file"



# ===================================判断字符串是否是Unicode字符: isinstance(s, unicode)====================== 
#str_1 = u"中文unicode"     #指定一个unicode字符串
str_1 = "中文unicode"       #指定一个普通字符串，因为系统默认是ascii编码， 但为了显示中文，#coding='utf8'强制为utf8编码

#获取字符串的编码方式
print str_1.__class__           # 可获取字符串的type，是普通字符串str 还是 unicode?

#获取系统的 locale
lang = string.upper(locale.setlocale(locale.LC_ALL, ""))
print lang

#获取系统的 默认编码,为ascii
print sys.getdefaultencoding()

#判断是否是unicode, 并作相应转换
if isinstance(str_1, unicode):
    print "this is an unicode: %s" %str_1
    print "unicode <=> gb2312: %s" %str_1.encode('gb2312')
else:
    print "this is not an unicode: %s" %str_1

    utf8_unicode = str_1.decode('utf8')             # 或者 unicode(str_1, utf8), 因为系统默认编码是utf8, 此处将utf8通过decode或unicode转化成unicode
    print "utf8 <=> unicode: %s" %utf8_unicode  

    unicode_utf8 = utf8_unicode.encode('gb2312')    # 此处将unicode通过encode转化成gb2312
    print "unicode <=> gb2312: %s" %unicode_utf8



# ===============================控制大小写 upper, lower, swapcase, title, capitalize =====================================
str_2 = "Hello, This will be changed"
print "Oringal: %s" %str_2

print str_2.upper()         #upper不带参数，转换为大写
print str_2.lower()         #lower不带参数，转换为小写
print str_2.swapcase()      #swapcase不表参数，大小定互换
print str_2.title()         #title不带参数，把每一个单词的首字母转换为大写，其余转换为小写
print str_2.capitalize()    #capitalize不带参数，把整个字符的首字母转换为大写，其余转换为小写

#判断大小写: isupper, islower, istitle, 也都不带参数
if str_2[0].isupper():
    print "this is an upper string"
if str_2[1].islower():
    print "this is a lower string"
if str_2[0:4].title():
    print "this is a title string"

# 但是没有 iscapitalize()方法， 可以自己写一个简单的函数来判断
def iscapitalize(s):
    return s == s.capitalize()

str_cap = "My name is hongsun"
if iscapitalize(str_cap):
    print "this is a capitalize string"
else:
    print "this is not a capitalize string"




# ===================================== 使用struct模块来封装解析ctype数据类型 ==================
#struct模块中最重要的三个函数是pack(), unpack(), calcsize()
#pack(fmt, v1, v2, ...)    按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)
#unpack(fmt, string)       按照给定的格式(fmt)解析字节流string，返回解析出来的tuple
#calcsize(fmt)             计算给定的格式(fmt)占用多少字节的内存

# id, tag, version, count = struct.unpack("!H4s2I", s)  
# 通过socket.recv接收到了一个结构体数据，存在字符串s中，现在需要把它解析出来，可以使用unpack()函数
# !表示我们要使用网络字节顺序解析，因为我们的数据是从网络中接收到的，在网络上传送的时候它是网络字节顺序的.
# 后面的H表示一个unsigned short的id,4s表示4字节长的字符串，2I表示有两个unsigned int类型的数据.
# 这样通过一个unpack，现在id, tag, version, count里已经保存好我们的信息了.

# ss = struct.pack("!H4s2I", id, tag, version, count) 
# pack函数就把id, tag, version, count按照指定的格式转换成了结构体Header，
# ss现在是一个字符串(实际上是类似于c结构体的字节流)，可以通过 socket.send(ss)把这个字符串发送出去.

buffer = struct.pack('ihb', 1, 2, 3)
print repr(buffer)
print struct.unpack('ihb', buffer)

#请注意下面的 *data 的应用, 此处的 * 号表示位置参数，把参数收集到一个元组中 
#data = (1, 2, 3)
data = [1, 2, 3]
buffer = struct.pack('!ihb', *data)
print repr(buffer)
print struct.unpack('!ihb', buffer)



# ====================================== 使用struct模块unpack的format功能来提取一条记录中想要的字段数据 =================
# 取前5个字符，跳过4个字符华，再取3个字符, 返回一个元组
format = '5s 4x 3s' 
str = "Test astring"
print struct.unpack(format, str)
print 

# 字符串'He is not very happy'，处理一下，把中间的not去掉，然后再输出
theString = 'He is not very happy'
format = '2s 1x 2s 5x 4s 1x 5s'
print struct.unpack(format, theString)
print ' '.join(struct.unpack(format, theString)) 




#===============================在一个多行的文本字符串 行首添加指定数目的空格，以满足缩进 =================================
text_string = '''    ----Beging----
     what is lead?
      linux suse
       -----End-----'''
print text_string
print "\n"

def reindent(s, numSpaces):
    leading_space = ' ' * numSpaces
    # 这个for循环写法很神奇，解决了for完以后，lines得到的就是一个元组数据,而不是单一的一个值
    return '\n'.join(leading_space + line.strip() for line in s.splitlines())

print reindent(text_string, 4)
print "\n"



# ===============================保留当前每行之间的缩进比例，同时在行首添加指定数目的空格，以扩展缩进 =====================
def addSpaces(s, numAdd):
    white = ' ' * numAdd
    return white + white.join(s.splitlines(True))   # 此处不用for来循环，是因为没有对每行strip，而splitlines为True，表示split时，保留空格

print addSpaces(text_string, 4)
print "\n"



# ===============================保留当前每行之间的缩进比例，同时在行首删除指定数目的空格，以压缩缩进 ====================
# 需要检查每行行首的空格，以确保不会把非空格字符截去
def numSpaces(s):
    return [len(line) - len(line.lstrip()) for line in s.splitlines()]

def delSpaces(s, numDel):
    if numDel > min(numSpaces(s)):
        raise ValueError('number must be non-negative')     #此处用raise来捕获异常
    return '\n'.join( line[numDel:] for line in s.splitlines() )

print delSpaces(text_string, 3)
print "\n"



# ==================================将制表符tab转换成一定数目的空格,expandtabs() =============================
# 用python提供的expandtabs方法可轻松解决，由于字符串不能被改变，这个方法返回一个新的字符串对像， 是原字符串修改过的一个拷贝
# 不过，仍可以把修改过的字符串绑定到原字符串的名字, 这不会改变原字符串名字指向的字符串对象，只不过是名字绑定到一个新创建的字符对象上
# expandtabs 默认制表符的宽度是8，可以给expandtabs来传递参数重新指定制表符宽度
# python 中推荐使用标准的4个空格来代替tab
string_tab = "	expandtabs"
print string_tab.expandtabs(1)
print "\n"



# =============================== string.Template() 指定替换 ======================
# 从字符串生成模板，用 $ 标记需要作为模板的字符
new_style = string.Template('this is $thing')
# 给模板的substitute 方法传入一个字典参数，并调用 
print new_style.substitute({'thing':5})
print new_style.substitute({'thing':'a string.Template'})

# 也可以给模板的substitute 方法传递关键字参数
print new_style.substitute(thing = 'substitute')
print new_style.substitute(thing = 12345)
print '\n'

# 被 $$ 标记的，将不会被替换
format_string = '''+ $Added category and summary to patterns
+ $Removed kernel-default and the KMPs of default flavor
- only pae entry in $$grub
+ $Added a new pattern for LSI modem'''

new_template = string.Template(format_string)
print new_template.substitute(Added='Removed', Removed='Added', grub='grub2')


# =================================== map() 与 imap() 来检查字符串的结束标记 =======================
# map 返回一个列表， 此处map调用filename.endswith来接受参数, endswith将返回True或False 
def anyTrue_map(func, seq):
    if True in map(func, seq):
        return True
    else:
        return False

print os.listdir('.')
for filename in os.listdir('.'):
    if anyTrue_map(filename.endswith, (".swp", ".txt")):
        print filename

# 也可以用迭代器itertools的imap方法来代替 map, imap和map不同的是，imap返回的是一个iteration对象，而map返回的是一个list对象
def anyTrue_imap(func, seq):
    if True in itertools.imap(func, seq):
        return True
    else:
        return False

for filename in os.listdir('.'):
    print anyTrue_imap(filename.endswith, ('.py', '.txt'))
    if anyTrue_imap(filename.endswith, ('.py', '.txt')):
        print filename





# ==================================切片，步长============================
# 字符串、列表、元组在python中都符合“序列”这一特征，只要符合这一特征的变量我们都可以用切片(slice)去存取它们的任意部分。
# 切片操作符在python中的原型是  [start:stop:step], 即：[开始索引:结束索引:步长值]
# 开始索引：同其它语言一样，从0开始。序列从左向右方向中，第一个值的索引为0,最后一个为-1
# 结束索引：切片操作符将取到该索引为止，不包含该索引的值。
# 步长值：默认是一个接着一个切取，如果为2,则表示进行隔一取一操作; 步长值为正时表示从左向右取; 如果为负，则表示从右向左取。步长值不能为0
str = "Hello World"
print str[1:]   	#省略终止索引，表示取起始索引之后的所有值
print str[:3]           #省略起始索引，表示从0开始取，等效于str[0:3]
print str[:]            #省略起始索引、终止索引、步长值表示取全部
print str[::]           #省略起始索引、终止索引、步长值表示取全部
print str[::-1]         #省略起始索引、终止索引，步长值为-1，表示反向获取




# ===================================正则表达式 re ==========================
#   .       匹配除换行符之外的任意一个单个字符 
#   ^       匹配一个字符串的开头
#   $       匹配一个字符串的末尾

#   *       前一个字符可以被匹配零次或更多次,所以根本就可以不出现; ca*t 将匹配 "ct" (0 个 "a" 字符), "cat" (1 个 "a"), "caaat" (3 个 "a" 字符)
#   +       前一个字符可以被匹配一次或更多次, + 则要求至少出现一次
#   ?       前一个字符可以被匹配一次或零次, 它用于标识某事物是可选的, 例如：home-?brew 匹配 "homebrew" 或 "home-brew"。
#   {m}     精确重复匹配前表达式m次
#   {m,}    至少重复匹配前表达式m次
#   {m,n}   前一个字符至少有 m 个重复，至多到 n 个重复。举个例子，a/{1,3}b 将匹配 "a/b"，"a//b" 和 "a///b"

#   [...]   匹配集合内的字符，如[a-z],[1-9]或[,./;'] 
#   [^...]  匹配除集合外的所有字符，相当于取反操作
#   A|B     匹配表达式A或B，相当于OR操作;  为了匹配字母 "|"，可以用 \|，或将其包含在字符类中，如[|]
#   ()      表达式分组，每对括号为一组，如([a-b]+)([A-Z]+)([1-9]+)

#   \       反斜杠后面可以加不同的字符以表示不同特殊意义; 也可以用于取消所有的元字符，如匹配字符 "[" 或 "\"，可以在它们之前用反斜杠来取消它们的特殊意义： \[ 或 \\
#   \d      匹配任何十进制数；它相当于类 [0-9]。
#   \D      匹配任何非数字字符；它相当于类 [^0-9]。
#   \s      匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
#   \S      匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
#   \w      匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
#   \W      匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。


#   \A      只匹配字符串首; 在多行模式里\A 也只是匹配字符串首，而 ^ 还可以匹配在换行符之后字符串的任何位置
#   \Z      只匹配字符串尾
#   \b      单词边界, 只用以匹配单词的词首和词尾
#   \B      匹配不位于开头或者结尾的空字符串 

#   Python 的 raw 取消反斜杠转义功能:
#   在字符串前加个 "r" 反斜杠就不会被任何特殊方式处理
#   所以 r"\n" 就是包含"\" 和 "n" 的两个字符，而 "\n" 则是一个字符，表示一个换行。


# re 所定义的 flag 包括：
#   re.I 忽略大小写
#   re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
#   re.M 多行模式
#   re.S 即为’ . ’并且包括换行符在内的任意字符（’ . ’不包括换行符）
#   re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
#   re.X 为了增加可读性，忽略空格和’ # ’后面的注释

# re.match() 只从字串的开始位置进行匹配，如果失败，它就此放弃:
# 函数原型： re.match(pattern, string, flags)
#       group() 返回被 RE 匹配的字符串
#       start() 返回匹配开始的位置
#       end()   返回匹配结束的位置
#       span()  返回一个元组包含匹配 (开始,结束) 的位置 

text = "Test re.match() function"
match = re.match(r"(\w+)\s", text, re.I)
if match:
    print "match.group: %s" %match.group()
    print "match.start: %s" %match.start()
    print "match.end: %s" %match.end()
    print "match.span:",  match.span()
    print "The first string is: %s" %match.group()
else:
    print "Not Match"


# re.search() 则会锲而不舍地完全遍历整个字串中所有可能的位置，直到成功地找到一个匹配，或者搜索完字串，以失败告终
# 函数原型： re.search(pattern, string, flags)
text = "re.search() oo checked"
search = re.search(r"checked", text, re.I)
if search:
    print "search.group: %s" %search.group(0)
    print "search.start: %s" %search.start()
    print "search.end: %s" %search.end()
    print "search.span:", search.span()
    print "The search string is %s" %search.group()
else:
    print "Not Match"


# re.findall() 在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
# 从一堆文本中，找出所有可能的匹配，以列表的形式返回，这种情况用findall()这个函数
# 函数原型： re.findall(pattern, string[, flags])
text ='''sun@novell.com Preload QA team hongsun@gmail.com weekly meeting
Automation test traing'''
findall = re.findall(r'\w+@\w+.\w+', text, re.S)
print "the findall list is: %s" %findall


# re.split() 将字符串匹配正则表达式的部分割开并返回一个列表
# 函数原型： re.split(pattern, string[, maxsplit=0, flags=0])
text = "root:x:0:0:root:/root:/bin/bash"
split = re.split(r':', text)
print split
print ','.join(split)

# 一般对于含有多种分隔符的字串， 先替换成一个统一的字符， 可用内建的replace()来更好的完成替换
text = "str1 | str2, & str3  &&,|& str4"
result = re.sub(r'&|,|\|', ' ', text)
split = re.split('\s+', result)
print result
print split

# re.sub() 查找替换, 返回被修改完的字串
# 函数原型： re.sub(pattern, repl, string[, count, flags])
# 在字符串 string 中找到匹配正则表达式 pattern 的所有子串，用另一个字符串 repl 进行替换
# 如果没有找到匹配 pattern 的串，则返回未被修改的 string
# Repl 既可以是字符串也可以是一个函数
text = "JGood is a handsome boy, he is cool, clever, and so on..."  
print re.sub(r'\s+', '-', text)  


# re.subn() 查找替换，返回被修改完的字串和替换的次数
# re.subn(pattern, repl, string[, count, flags])
# 该函数的功能和 sub() 相同，但它还返回新的字符串以及替换的次数
# 替换所有匹配的子串: subn 返回一个元组 (new_string, n) ,这里n是subn替换的次数 
text = "JGood is a handsome boy, he is cool, clever, and so on..."  
result, number = re.subn(r'\s+', '+', text)
print "the result is: %s" %result
print "the number is: %d" %number


# 最小匹配 *? +? ??
s =r"/* every so often */ update a block */"
print re.findall( r'/\*.*\*/' , s )
print re.findall( r'/\*.*?\*/' , s )
print "\n"


# 前向界定和后向界定: 有时候需要匹配一个跟在特定内容后面的或者在特定内容前面的字符串，Python提供一个简便的前向界定和后向界定功能：
#    '(?<=...)' 前向界定:  括号中'...' 代表你希望匹配的字符串的前面应该出现的字符串
#    '(?=...)'  后向界定:  括号中'...' 代表你希望匹配的字符串的后面应该出现的字符串
# 找出c语言的注释中的内容/*........*/
c_string = '''/* every so often,*/ update a block */
/* update this block */
/* touch a word */'''
print re.findall( r'/\*.*?\*/' , c_string )
print re.findall( r'(?<=/\*).*(?=\*/)', c_string)
print re.findall( r'(?<=/\*).*?(?=\*/)', c_string)

# 前向界定括号中的表达式必须是常值，也即你不可以在前向界定的括号里写正则式
# 如在下面的字符串中, 想找到被字母夹在中间的数字，不可以用前向界定： (?=<[a-z]+)
# s = 'aaa111aaa, bbb222, 333ccc '
# print re.findall( r'(?<=[a-z]+)\d+(?=[a-z]+)' , s )

# 不过后向界定, 可以用正则式, 下面后向界定将找出后面接着有字母的数字:
s = 'aaa111aaa, bbb222, 333ccc'
print re.findall(r'\d+(?=[a-z]+)', s)

# 如果一定要匹配包夹在字母中间的数字，可以使用组（group）的方式:
s = 'aaa111aaa, bbb222, 333ccc'
print re.findall(r'[a-z]+(\d+)[a-z]+', s)


# 前向非界定和后向非界定： 
#    '(?<!...)' 前向非界定, 只有当你希望的字符串前面不是'...'的内容时才匹配
#    '(?!...)'  后向非界定, 只有当你希望的字符串后面不是'...'的内容时才匹配
#希望匹配后面不跟着字母的数字, 使用了\w而不是像上面那样用[a-z]
s = 'aa111aaa, bbb222, 333ccc'
print re.findall(r'\d+(?!\w+)', s)


#  '(' ')'  无命名组
#   最基本的组是由一对圆括号括起来的正则式, 比如上面匹配包夹在字母中间的数字的例子, 使用的(\d+)
#   看到findall函数只返回了包含在'()'中的内容，而虽然前面和后面的内容都匹配成功了，却并不包含在结果中
s = 'aaa111aaa, bbb222, 333ccc'
print re.findall(r'[a-z]+(\d+)[a-z]+', s)

#   '(?P<name>…)’ 命名组
#   ?P     代表这是一个Python的语法扩展
#   <name> 里面是给这个组起的名字，比如你可以给一个全部由数字组成的组叫做'num'，它的形式就是'(?P<num"\d+)'
#   起了名字之后，我们就可以在后面的正则式中通过名字调用这个组，它的形式是: '(?P=name)' 调用已匹配的命名组

s='aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
print re.findall(r'([a-z]+)\d+([a-z]+)', s)         # 找出中间夹有数字的字母
print re.findall(r'(?P<g1>[a-z]+)\d+(?P=g1)', s)    # 找出中间夹有数字, 前后字母一样，取这个一样的字符
print re.findall(r'[a-z]+(\d+)([a-z]+)', s)         # 找出前面有字母引导，中间是数字，后面是字母, 取中间的数字和后面的字母


# 上面名字也不是必需的, 也可以通过序号调用已匹配的组: '\number'
# 正则式中的每个组都有一个序号，序号是按组从左到右，从1开始的数字，如上面找出被中间夹有数字, 前后同样的字母的例子，也可以写成：
s='aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
print re.findall(r'([a-z]+)\d+\1', s)

# 找出完全对称的 数字－字母－数字－字母－数字 中的数字和字母
s='111aaa222aaa111 , 333bbb444bb33'
print re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)', s)


#'(?:)' 无捕获组
s='ababab abbabb aabaab'
print re.findall(r'\b(?:ab)+\b', s)

#'(?# )' 注释
#Python允许你在正则表达式中写入注释，在’(?#’ ‘)’之间的内容将被忽略


# 匹配汉字等字符
# utf8下，每个汉字占据3个字符位置，正则式为[\x80-\xff]{3}
# unicode下，汉字的格式如\uXXXX，只要找到对应的字符集的范围，就能匹配相应的字串



# =======================================================================================================


# 字符串string表现形式:
#   'me'单引号
#   "me"双引号 
#   '''me'''三引号，这个一般用来写多行文本。__doc__使用这个
#   r"me", 在字符串前面添加一个r，raw的缩写，就是原生字符（关掉字符串中的转义, Python中还有一个函数有一样的功能rept()。
#   u"Python语法String的操作"，指明这是一个unicode字符


# String是一个序列:
#   String是一个序列，而且是一个不可变（Immutable）。既然String是一个序列，很自然的就相到可以使用Slice
#   S[1:9:2] 这个是感觉很奇怪的东西，其实2这里是步长的意思
#   S[::-1] 这个可以将一个字符反转, 就是"abc"变成"cba",但如果是中文，反了就成乱码啦
#   字符串直接可以同"+"的方式来连接 


# 字符串中字符大小写的变换：
#S.lower() #小写
#S.upper() #大写
#S.swapcase() #大小写互换
#S.capitalize() #首字母大写
#S.title() #只有首字母大写，其余为小写，模块中没有这个方法 


#字符串在输出时的对齐：
#S.ljust(width,[fillchar])   #输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格。
#S.rjust(width,[fillchar])   #右对齐
#S.center(width, [fillchar]) #中间对齐
#S.zfill(width)              #把S变成width长，并在右对齐，不足部分用0补足 


#字符串中的搜索和替换：
#S.find(substr, [start, [end]])      #返回S中出现substr的第一个字母的标号，如果S中没有substr则返回-1。start和end作用就相当于在S[start:end]中搜索
#S.index(substr, [start, [end]])     #与find()相同，只是在S中没有substr时，会返回一个运行时错误
#S.rfind(substr, [start, [end]])     #返回S中最后出现的substr的第一个字母的标号，如果S中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号
#S.rindex(substr, [start, [end]])

#S.count(substr, [start, [end]])     #计算substr在S中出现的次数
#S.replace(oldstr, newstr, [count])  #把S中的oldstar替换为newstr，count为替换次数。这是替换的通用形式，还有一些函数进行特殊字符的替换
#S.strip([chars])                    #把S中前后chars中有的字符全部去掉，可以理解为把S前后chars替换为None
#S.lstrip([chars])
#S.rstrip([chars])
#S.expandtabs([tabsize])             #把S中的tab字符替换没空格，每个tab替换为tabsize个空格，默认是8个 

find_string = '''Your mail concerning "Re: Certification weekly meeting summarY"
has reached me, and will be read when I am back.  '''

if find_string.find("Cedrtifications"):
    print "find Certification"

print find_string.count('ee')

print find_string.replace('"', ' ')



#字符串的分割和组合：
#S.split([sep, [maxsplit]])          #以sep为分隔符，把S分成一个list。maxsplit表示分割的次数。默认的分割符为空白字符
#S.rsplit([sep, [maxsplit]])
#S.splitlines([keepends])            #把S按照行分割符分为一个list，keepends是一个bool值，如果为真每行后而会保留行分割符。
#S.join(seq)                         #把seq代表的序列──字符串序列，用S连接起来 


#字符串的mapping，这一功能包含两个函数：
#String.maketrans(from, to)          #返回一个256个字符组成的翻译表，其中from中的字符被一一对应地转换成to，所以from和to必须是等长的。
#S.translate(table[,deletechars])


#字符串还有一对编码和解码的函数：
#S.encode([encoding,[errors]])       # 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持
#S.decode([encoding,[errors]]) 


#字符串的测试函数，这一类函数在string模块中没有，这些函数返回的都是bool值：
#S.startswith(prefix[,start[,end]])   #是否以prefix开头
#S.endswith(suffix[,start[,end]])     #以suffix结尾

#S.isalnum()                         #是否全是字母和数字，并至少有一个字符
#S.isalpha()     #是否全是字母，并至少有一个字符
#S.isdigit()     #是否全是数字，并至少有一个字符
#S.isspace()     #是否全是空白字符，并至少有一个字符
#S.islower()     #S中的字母是否全是小写
#S.isupper()     #S中的字母是否便是大写
#S.istitle()     #S是否是首字母大写的 



#字符串类型转换函数，这几个函数只在string模块中有：
#string.atoi(s[,base])   #base默认为10，如果为0,那么s就可以是012或0x23这种形式的字符串，如果是16那么s就只能是0x23或0X12这种形式的字符串
#string.atol(s[,base])   #转成long
#string.atof(s[,base])   #转成float 


