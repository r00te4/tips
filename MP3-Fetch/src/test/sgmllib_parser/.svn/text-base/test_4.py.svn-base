#!/usr/bin/python

from sgmllib import SGMLParser
import urllib, urllib2, sys

class myparser(SGMLParser):
    is_td=0
    is_prices=0
    is_song_name = 0
    
    def __init__(self):
        SGMLParser.__init__(self)

    def start_table(self, attrs):
        for id,value in attrs:
            if id=='class' and value=='table-song-list' :
                self.is_prices=1
    
    def end_table(self):
        self.is_prices=0

    def start_td(self, attrs):
        for song_name, song_value in attrs:
            if song_name == "class" and song_value == "second":
                self.is_song_name = 1

    def end_td(self):
        self.is_song_name = 0

    def handle_data(self, text):
        if self.is_prices==1 and self.is_song_name==1:
            self.is_song_name = 1
            print text

    def start_a(self, attrs):
        if self.is_song_name==1:
            for href_name, href_value in attrs:
                if href_name == "href":
                    print href_value

urllink=urllib2.urlopen('http://mp3.baidu.com/m?rf=top-index&tn=baidump3&ct=134217728&word=forever%2021+%D4%F8%E9%F3%BF%C9&lm=-1')
data=urllink.read()

sys_encode = sys.getfilesystemencoding()
data = data.decode('gbk').encode(sys_encode)
urllink.close()

my=myparser()
my.feed(data)

