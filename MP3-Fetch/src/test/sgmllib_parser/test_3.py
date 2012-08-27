#!/usr/bin/python

from sgmllib import SGMLParser
import urllib

class myparser(SGMLParser):
    is_td=0
    is_prices=0
    
    def __init__(self):
        SGMLParser.__init__(self)

    def start_div(self, attrs):
        for id,value in attrs:
            if id=='id' and value=='prices' :
                self.is_prices=1
        #if attrs[0][1]=='prices':
            #self.is_prices=1
    
    def end_div(self):
        self.is_prices=0

    def start_td(self, attrs):
        self.is_td=1

    def end_td(self):
        self.is_td=0

    def handle_data(self, text):
        if self.is_prices==1 and self.is_td==1:
            #print text.decode('cp936')
            print text

urllink=urllib.urlopen('http://www.google.cn/finance/historical?q=SHA:000001')
data=urllink.read()
urllink.close()

my=myparser()
my.feed(data)

