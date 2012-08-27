#! /usr/bin/python
#coding=utf8

data = '''
<table class="table-list" cellpadding="0" cellspacing="0" border="0">
   <tr class="own">
       <td class="first"> <a href="http://www.baidu.com" target="_blank"><em>百度</em></a> </td>
       <td class="second"><a href="http://news.baidu.com" target="_blank"><em>新闻</em></a></td>
    </tr>
   <tr class="own stripe">
       <td class="first"> <a href="http://www.sina.com" target="_blank"><em>新浪</em></a> </td>
       <td class="second"><a href="http://news.sina.com" target="_blank"><em>新闻</em></a></td>
    </tr>
</table
'''
#1. 需要定位到class="table-list" 的这个table
#2. 需要提取这个table的文本数据,以及对应的href 

from sgmllib import SGMLParser
import urllib2, sys

class table_parser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.is_table_list = 0
        self.is_td_second = 0
        self.url_list = []
        self.text_list = []

    def start_table(self, attrs):
        for id, value in attrs:
            if id == "class" and value == "table-song-list":
                self.is_table_list = 1
    def end_table(self):
        self.is_table_list = 0

    def start_td(self, attrs):
        for id, value in attrs:
            if id == "class" and value == "second":
                self.is_td_second = 1
    def end_td(self):
        self.is_td_second = 0

    def handle_data(self, data):
        if self.is_table_list == 1 and self.is_td_second == 1:
            self.text_list.append(data)

    def start_a(self, attrs):
        if self.is_td_second == 1:          #这里是关键的关键, 不知道为什么不能写成: if self.is_table_list and self.is_td_second == 1 
             for id, value in attrs:
                if id == "href":
                    self.url_list.append(value)

url = "http://mp3.baidu.com/m?rf=top-index&tn=baidump3&ct=134217728&word=forever%2021+%D4%F8%E9%F3%BF%C9&lm=-1"
req = urllib2.Request(url)
fd = urllib2.urlopen(req)
html = fd.read()

sys_encode = sys.getfilesystemencoding()
html = html.decode("gbk").encode(sys_encode)


t_parser = table_parser()
t_parser.feed(html)

for url in t_parser.url_list:
    print url.strip()

for text in t_parser.text_list:
    print text.strip()
