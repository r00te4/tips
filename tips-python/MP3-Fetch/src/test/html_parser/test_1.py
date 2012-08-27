#! /usr/bin/python
#coding=utf8

from HTMLParser import HTMLParser
import urllib2, sys
 
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

class MyHTMLParser(HTMLParser):
    def reset(self):
        HTMLParser.reset(self)
        self.is_table_list = 0
        self. is_td_second = 0
 
    def handle_starttag(self, tag, attrs):
        if tag == "table":
            for id, value in attrs:
                if id == "class" and value == "table-song-list":
                    self.is_table_list = 1
          
        if tag == "td":
            for id, value in attrs:
                if id == "class" and value == "second":
                    self.is_td_second = 1

        if tag == "a":
            if self.is_td_second == 1:
                for id, value in attrs:
                    if id == "href":
                        print value

    def handle_endtag(self, tag):
        if tag == "table":
            self.is_table_list = 0
        if tag == "td":
            self.is_td_second = 0

    def handle_data(self, data):
        if self.is_table_list == 1 and self.is_td_second == 1:
            print data
 
if __name__ == "__main__":

    url = "http://mp3.baidu.com/m?rf=top-index&tn=baidump3&ct=134217728&word=forever%2021+%D4%F8%E9%F3%BF%C9&lm=-1"
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    html = fd.read()

    sys_encode = sys.getfilesystemencoding()
    html = html.decode("gbk").encode(sys_encode)

    hp = MyHTMLParser()
    hp.feed(html)
