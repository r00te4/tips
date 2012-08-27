#!/usr/bin/env python
import urllib2
import sys
from sgmllib import SGMLParser

class Parse(SGMLParser):
    def reset(self):
        self.found_tr = 0
        SGMLParser.reset(self)

    def start_tr(self, attrs):
        self.found_tr += 1

    def end_tr(self):
        self.found_tr -= 1

    def handle_data(self, text):
        if self.found_tr > 0:
            print 'Data: %s' % text

url = "http://mp3.baidu.com/m?rf=top-index&tn=baidump3&ct=134217728&word=%D7%EE%D4%B6%B5%C4%BE%E0%C0%EB+%C9%B3%B1%A6%C1%C1&lm=-1"

def GBK_Unicode_Syscode(html):
    syscode = sys.getfilesystemencoding()
    html = html.decode('gbk'  ).encode(syscode)
    return html

fp = urllib2.urlopen(url)
html = fp.read()
html = GBK_Unicode_Syscode(html)

p = Parse()
p.feed(html)
