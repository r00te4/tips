#! /usr/bin/python
#!coding=utf8
'''
#=============================================================================
#     FileName:		baidu.py
#     Desc:	        Download baidu top100 and top500 mp3 audio, thread pool, parser html table
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-07-25 10:49:26
#     History:		
#=============================================================================
'''

import urllib, urllib2, HTMLParser, urlparse
from sgmllib import SGMLParser
from optparse import OptionParser
import os, sys, re
import threading
import Queue
import pycurl
import StringIO

class Mythread(threading.Thread):
    def run(self):
        while True:
            queue_data = queue.get()
            song_dir = queue_data[0]
            song_name = queue_data[1]
            song_url = queue_data[2]
            if not song_url:
                break
            thread_list.append(Do_Process_URL(song_dir, song_name, song_url))
            queue.task_done()

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []
        
    def start_a(self, attrs):
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

# 将GBK的网页编码转换成系统编码能识别的网页
def GBK_Unicode_Syscode(html):
    try:
        syscode = sys.getfilesystemencoding()
        html = html.decode('gbk').encode(syscode)
        return html
    except:
        pass

# 使用SGMLParser, 提取网页中是Top100 MP3 的所有的URL
def Parser_All_URL(html):
    parser = URLLister()
    parser.feed(html)
    for url in parser.urls:
        all_orig_url.append(url)


# 对Parser_All_URL提取的所有Top100 URL, 因为URL含有中文字符, 使用urllib.quoto对每一个URL进行编码转换
def Split_URL(all_orig_url):
    for url_top_page in all_orig_url:
        search = re.search(r"top-index&tn=baidump3", url_top_page, re.S)
        if search:
            split_url = url_top_page.split("word=") 
            split_word_1 = split_url[1]
            split_word_2 = split_word_1.split("&lm=")
            split_word_3 = split_word_2[0]
            split_word_4 = split_word_3.split("+")

            song = split_word_4[0]
            quote_song = urllib.quote(song.decode(sys.stdin.encoding).encode('gbk'))

            singer = split_word_4[1]
            quote_singer = urllib.quote(singer.decode(sys.stdin.encoding).encode('gbk'))

            new_word = "word="+quote_song.strip()+"+"+quote_singer.strip()
            new_url = split_url[0]+new_word+"&lm"+split_word_2[1]

            song_name = song
            song_name_url_dict[song_name] = new_url

# 对html中的表格进行处理, 所处理的表格含有关键字:table-song-list, 先提取<table>层,再提取<tr>层,最后获得<td>层数据
def Table_Song_List(url, html):
    song_list_downlink = []
    #print "Start to Parser Table from ", url
    table_data = re.findall(r'(?<=<table class="table-song-list")[\s\S]*?(?=</table>)', html)

    if len(table_data):
        tr_data = re.findall(r'(?<=<tr)[\s\S]*?(?=</tr>)', table_data[0])

        for td_item in tr_data:
            td_data = re.findall(r'(?<=<td)[\s\S]*?(?=</td>)', td_item)

            if len(td_data) == 8:    
                #歌曲名 及 歌曲下载地址, td_data[0]
                td_song_herf = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[0])
                if len(td_song_herf) == 0:
                    td_song_herf.append("No URL Found!")
                                                
                td_song_name = re.findall(r'(?<=<em>)[\s\S]*?(?=</em>)', td_data[0])
                if len(td_song_name) == 0:
                    td_song_name = re.findall(r' (?<=;">)[\s\S]*?(?=</a>)' , td_data[0])
                    if len(td_song_name) == 0:
                        td_song_name.append("Unknown")

                #歌手名 及歌手地址, td_data[1]
                td_singer_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[1])
                td_singer_name = re.findall(r'(?<=<em>)[\s\S]*?(?=</em>)', td_data[1])
                if len(td_singer_name) == 0:
                    td_singer_name.append("Unknown")

                #专辑 及专辑地址, td_data[2]
                td_album_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[2])
                td_album_name = re.findall(r'(?<=<em>)[\s\S]*?(?=</em>)', td_data[2])

                #试听地址, td_data[3]
                td_listen_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[3])

                #歌词地址, td_data[4]
                td_lrc_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[4])

                #歌曲下载地址, td_data[5]
                td_download_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[5])

                #歌曲格式, td_data[6]
                td_format = re.findall(r'(?<=<span>)[\s\S]*?(?=</span>)', td_data[6])
                if len(td_format) == 0:
                    td_format.append("Unknown")

                #歌曲大小, td_data[7]
                td_size = re.findall(r'(?<=<span>)[\s\S]*?(?=</span>)', td_data[7])
                if len(td_size) == 0:
                    td_size.append("Unknown")
        
                for td_song_name_item in td_song_name:
                    get_td_song_name = td_song_name_item
                for td_singer_name_item in td_singer_name:
                    get_td_singer_name = td_singer_name_item
                for td_size_item in td_size:
                    get_td_size = td_size_item
                for td_format_item in td_format:
                    get_td_format = td_format_item
                for td_song_herf_item in td_song_herf:
                    get_td_song_herf =td_song_herf_item

                song_item = get_td_song_name+'_'+get_td_singer_name+'_'+get_td_size+'.'+get_td_format+'____'+get_td_song_herf
                song_list_downlink.append(song_item)
                #break
            
            if len(td_data) == 9:
                #歌曲名 及 歌曲下载地址, td_data[1]
                td_song_herf = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[1])
                if len(td_song_herf) == 0:
                    td_song_herf.append("No URL Found!")
                td_song_name = re.findall(r'(?<=<em>)[\s\S]*?(?=</em>)', td_data[1])
                if len(td_song_name) == 0:
                    td_song_name = re.findall(r' (?<=;">)[\s\S]*?(?=</a>)' , td_data[1])
                    if len(td_song_name) == 0:
                        td_song_name.append("Unknown")

                #歌手名 及歌手地址, td_data[2]
                td_singer_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[2])
                td_singer_name = re.findall(r'(?<=<em>)[\s\S]*?(?=</em>)', td_data[2])
                if len(td_singer_name) == 0:
                    td_singer_name.append("Unknown")

                #试听地址, td_data[4]
                td_listen_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[4])

                #歌词地址, td_data[5]
                td_lrc_href = re.findall(r'(?<=href=")[\s\S]*?(?=")', td_data[5])

                #歌曲格式, td_data[6]
                td_format = re.findall(r'(?<=<span>)[\s\S]*?(?=</span>)', td_data[6])
                if len(td_format) == 0:
                    td_format.append("Unknown")

                #歌曲大小, td_data[7]
                td_size = re.findall(r'(?<=<span>)[\s\S]*?(?=</span>)', td_data[7])
                if len(td_size) == 0:
                    td_size.append("Unknown")

                for td_song_name_item in td_song_name:
                    get_td_song_name = td_song_name_item
                for td_singer_name_item in td_singer_name:
                    get_td_singer_name = td_singer_name_item
                for td_size_item in td_size:
                    get_td_size = td_size_item
                for td_format_item in td_format:
                    get_td_format = td_format_item
                for td_song_herf_item in td_song_herf:
                   get_td_song_herf =td_song_herf_item

                song_item = get_td_song_name+'_'+get_td_singer_name+'_'+get_td_size+'.'+get_td_format+'____'+get_td_song_herf
                song_list_downlink.append(song_item)
                #break
    else:
        print "Can't find table-song-list from ", url

    return song_list_downlink


#处理Top100的MP3 URL, 分两层, 第一层搜索出所有可供下载的MP3列表, 第二层对每个URL跟踪可下载的地址
def Do_Process_URL(song_dir, song_singer, url):
    req = urllib2.urlopen(url)
    mp3_list_html = req.read()
    mp3_list_html = GBK_Unicode_Syscode(mp3_list_html)

    song_list_downlink = Table_Song_List(url, mp3_list_html)

    for song_list_downlink_item in song_list_downlink:
        song_item_split = song_list_downlink_item.split("____")
        song_singer_name = song_item_split[0]
        song_singer_url = song_item_split[1]
        
        down_html = Pycurl_HTML(song_singer_url)
        prefix = "http://mp3.baidu.com"

        try:
            down_href = re.findall( r'(?<=<a id="downlink" href=")[\s\S]*?(?=" onclick=)', down_html)
            down_encurl = re.findall( r'(?<=var encurl =)[\s\S]*?(?=, newurl)', down_html)
        except:
            pass

        if len(down_href):
            for down_href_item in down_href:
                down_addr = prefix + down_href_item 
            if Do_Download_pycurl(song_dir, song_singer_name, down_addr) == 0:
                break
        elif len(down_encurl):
            for down_encurl_item in down_encurl:
                encurl_replace = re.sub(r"'|\+| ", "", down_encurl_item)
                down_addr = encurl_replace
            if Do_Download_pycurl(song_dir, song_singer_name, down_addr) == 0:
                break
        else:
            print "No valaible download link for ", song_singer_url


#此处使用pycurl来获取html内容
def Pycurl_HTML(song_singer_url):
    text = StringIO.StringIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, song_singer_url)
    curl.setopt(pycurl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.MAXREDIRS, 5)
    curl.setopt(pycurl.CONNECTTIMEOUT, 30)
    curl.setopt(pycurl.TIMEOUT, 300)
    #curl.setopt(pycurl.HEADER, 1)
    curl.setopt(pycurl.WRITEFUNCTION, text.write)
    curl.setopt(pycurl.NOSIGNAL, 1)
    try:
        curl.perform()
        html=text.getvalue()
        html = GBK_Unicode_Syscode(html)
        http_code = curl.getinfo(curl.HTTP_CODE)
        if http_code == 400 or http_code == 401 or http_code ==404:
            pass
        return html
    except pycurl.error:
        pass

#每一首歌曲的一个地址, 尝试五次下载, 只要其中有一次下载成功, 则返回0结束; 
#如果五次都下载不成功,则轮循此首歌曲的下一个下载地址;
#如果该歌曲只有一个下载地址, 五次都下载失败的话,则些歌曲下载失败
def Do_Download_pycurl(song_dir, song_singer_name, down_addr):
    song_file = song_dir+song_singer_name

    for num in range(5):
        if os.path.exists(song_file):
            print "%s is existed already!" %song_singer_name
            return 0
        else:
            fp = open(song_file, "wb")
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, down_addr)
            curl.setopt(pycurl.FOLLOWLOCATION, 1)
            curl.setopt(pycurl.MAXREDIRS, 5)
            curl.setopt(pycurl.CONNECTTIMEOUT, 60)
            curl.setopt(pycurl.TIMEOUT, 300)
            #curl.setopt(pycurl.HEADER, 1)
            curl.setopt(pycurl.WRITEDATA, fp)
            curl.setopt(pycurl.NOSIGNAL, 1)

            try:
                print "Start to download %s from %s" %(song_file,down_addr)
                curl.perform()
                http_code = curl.getinfo(curl.HTTP_CODE)
                print http_code
                if http_code == 400 or http_code == 401 or http_code ==404:
                    print "Download failed: ", song_singer_name, down_addr
                    if os.path.exists(song_file):
                        os.remove(song_file)
                    if num == 2:
                        return 1
                else:
                    print "Download successful: ", song_singer_name
                    break

            except pycurl.error:
                print "Download Error: ", song_singer_name, down_addr
                if os.path.exists(song_file):
                    os.remove(song_file)
                if num == 2:
                    return 2
    return 0


if __name__ == "__main__":
    usage = "usage: %prog [options] arg1 arg2"
    version = "1.0"
    parser = OptionParser(usage=usage, version=version)

    parser.add_option("-a", "--top100", action="store_true", dest="top100", help="download baidu top_100 audio.")
    parser.add_option("-b", "--top500", action="store_true", dest="top500", help="download baidu top_500 audio.")
    parser.add_option("-t", "--thread_num",  dest="thread_num", help="defautl thread num is 10, please provide the thread num.")

    (options, args)=parser.parse_args()

    Thread_Num  =10
    url_addr_list = []
    all_orig_url = []
    song_name_url_dict = {}

    if options.top100:
        url_addr_list.append("http://list.mp3.baidu.com/top/top100.html")
        song_dir = "./baidu_top100_song/"
        if not os.path.exists(song_dir):
            os.makedirs(song_dir)
        else:
            pass

    if options.top500:
        url_addr_list.append("http://list.mp3.baidu.com/top/top500.html")
        song_dir = "./baidu_top500_song/"
        if not os.path.exists(song_dir):
            os.makedirs(song_dir)
        else:
            pass

    if options.thread_num:
        Thread_Num = options.thread_num 

    for url_addr_item in url_addr_list:
        print "Start to download: ", url_addr_item, "Thread Number is: ", Thread_Num
        f = urllib2.urlopen(url_addr_item)
        html = f.read()
        html = GBK_Unicode_Syscode(html)

        Parser_All_URL(html)
        Split_URL(all_orig_url)

        queue = Queue.Queue()
        thread_list = []

        for num in xrange(int(Thread_Num)):
            t = Mythread()
            t.setDaemon(1)
            t.start()

        for song_name, url in song_name_url_dict.items():
            queue.put((song_dir, song_name, url))

        queue.join()

