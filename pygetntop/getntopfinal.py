#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2,cookielib,string
from BeautifulSoup import BeautifulSoup
from datetime import *
import sys,urllib2,os,time 
import cookielib
import urllib
import urllib2
import re
import sys
url_login = 'http://f.10086.cn/im/login/inputpasssubmit1.action'
url_logout = 'http://f.10086.cn//im/index/logoutsubmit.action?t='
url_msg = 'http://f.10086.cn/im/user/sendMsgToMyselfs.action'
user = 'yourphonenumber'
password = 'yourpassword'
loginstatus = '4' 
arg_t = ''

def fetion(msg,fid):
    fetion_id=fid
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    args = {'pass':password, 'm':user,'loginstatus':loginstatus}
    print 'Logining...'
    req = urllib2.Request(url_login, urllib.urlencode(args))
    jump = opener.open(req)
    page = jump.read();
    url = re.compile(r'<card id="start".*?ontimer="(.*?);').findall(page)[0]             
    arg_t = re.compile(r't=(\d*)').findall(page)[0]
    if url == '/im/login/login.action':                                                   
        print 'Login Failed!'
        raw_input('Press any key to exit.')
        return
    else:
        print 'Login Successfully!'
        indexurl='http://f.10086.cn/im5/index/index.action?t=47852439005835570'
        indexreq=urllib2.Request(indexurl)
        indexfd=urllib2.urlopen(indexreq)
    while 1:
        indexdata=indexfd.read(1024)
        if not len(indexdata):
            break;
        #sys.stdout.write(indexdata)
        sys.stdout.write('hello')
    
    sendmsg = urllib2.Request(url_msg, urllib.urlencode({'msg':msg.decode('gbk').encode('utf-8')}))
    finish = urllib2.urlopen(sendmsg)
    wurl_msg='http://f.10086.cn/im/chat/sendMsg.action?touserid='+fetion_id
    sendmsgtowang=urllib2.Request(wurl_msg,urllib.urlencode({'msg':msg.decode('gbk').encode('utf-8')}))
    wfinish=urllib2.urlopen(sendmsgtowang)
    
    if wfinish.geturl=='http://f.10086.cn/im/chat/toinputMsg.action?touserid=718240484&t=50699214606073570':
       print 'Send ok'
    else:
        print 'Send Failed!'

    if finish.geturl == 'http://f.10086.cn/im/user/sendMsgToMyself.action' :
        print 'Send Self Failed!'
    else:
        print 'Send Self Failed'
    


def AlertToFetion(msgin):
    msg = msgin
    fid_list=['718240484',]
    for fid in fid_list:
        fetion(msg,fid)
        print "done!!!",fid,"~~~~~~~~~~~"











def readntop():
	try:
		ntopUrl="you ntop url"
		htmlSrc=urllib2.urlopen(ntopUrl).read()
		return htmlSrc
	except Exception,e:
		print (e)
	pass
def parsentop(htmlSrc):
	parser=BeautifulSoup(htmlSrc)
	all_traffic=parser.findAll('table')[8].findAll('tr')[1].find('td').contents
	mail_traffic=parser.findAll('table')[11].findAll('tr')[5].findAll('td')[0].contents
	http_traffic=parser.findAll('table')[11].findAll('tr')[1].findAll('td')[0].contents
	traffics=[''.join(all_traffic).replace("&nbsp;"," "),''.join(mail_traffic).replace("&nbsp;"," "),''.join(http_traffic).replace("&nbsp;"," ")]
	print traffics
	return traffics




htmlSrc=readntop()
trafficRes=parsentop(htmlSrc)
def showTraffic(trafficRes):
	today=datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
	trafficdetail="ALL----------"+trafficRes[0]+"\r\n"+"MAIL----------"+trafficRes[1]+"\r\n"+"HTTP----------"+trafficRes[2]+"\r\n"+today
	return trafficdetail
msg=showTraffic(trafficRes)
AlertToFetion(msg)




