#!/usr/bin/python
# -*- coding: utf-8 -*-
#import email,MySQLdb
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from time import sleep  
import smtplib
#import chardet
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding(),"~"*100
def sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText):

        strFrom = fromAdd
        strTo = ', '.join(toAdd)

        server = authInfo.get('server')
        user = authInfo.get('user')
        passwd = authInfo.get('password')

        if not (server and user and passwd) :
                print 'incomplete login info, exit now'
                return


        msgRoot = MIMEMultipart('related')
	msgRoot["Accept-Charset"]="ISO-8859-1,utf-8"
	msgRoot["Accept-Language"]="zh-CN"
        msgRoot['Subject'] = subject
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)


        msgText = MIMEText(plainText, 'plain', 'utf-8')
	msgText.set_charset("utf-8")
        msgAlternative.attach(msgText)
	
	msgText.set_charset("utf-8")
        msgText = MIMEText(htmlText, 'html', 'utf-8')
        msgAlternative.attach(msgText)


        fp = open('test.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
	print msgRoot.as_string()

	"""
        smtp =smtplib.SMTP(server, port=587, timeout=20)  

        smtp.ehlo()  
	smtp.starttls()                        
	smtp.ehlo()  
        smtp.login(user, passwd)
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	sleep(5) 
        smtp.quit()
	"""
        return

	

"""
def getMailInfo ():
	mailInfo=[]
	for ln in file('mail.ini','r') :
		infos=str(ln.strip().split('\n')).split('=')[1].rstrip("']")
		mailInfo.append(infos)		
		#print infos
	return mailInfo
"""


"""
def getMailContents(rankOper,rankValue):
	
	if rankOper=='gt':
		rankCondition='>='+rankValue

	elif rankOper=='lt':
		rankCondition='<='+rankValue


	MySQL_Server="localhost"
        MySQL_User="pymailtest"
	MySQL_Password="123456"
	MySQL_Database="pymail"  
	conn = MySQLdb.connect(MySQL_Server,MySQL_User,MySQL_Password,MySQL_Database,port=3306,connect_timeout=10,compress=True,charset='utf8',use_unicode=True)
	cursor=conn.cursor()
	vRank='SELECT * FROM `pymail_rank` where Score'+rankCondition
	cursor.execute(vRank)
	print vRank,"We select Info"
	rankRes=str(cursor.fetchone()[0])
	vInfo='SELECT * FROM `pymail_info` where Ranks_id='+rankRes+' order by id asc'
	InfoCount=cursor.execute(vInfo)
	print InfoCount
	infoRes=cursor.fetchmany(10)
	#infoRes=unicode(infoRes)
	print isinstance(infoRes,unicode),"is unicode"
	#print repr(infoRes).encode("gbk")
	#infosets=chardet.detect(str(infoRes))['encoding']
	#print infosets,"###"*20
	#print unicode(infoRes).encode("utf-8")
	print "*"*50
	mailTopics=[]
	mailSums=[]
	mailSources=[]
	htmls=[]
	
	for mailInfo in infoRes:
		#charsets=chardet.detect(unicode(repr(mailInfo),'ascii'))['encoding']
		#print charsets,"###"*10
		#print isinstance(mailInfo,unicode),"false  unicode"
		#mailInfo=unicode(mailInfo)
		
		print isinstance(mailInfo,unicode),"okay unicode"
		print mailInfo,"fucker"
		#print "~"*50,repr(mailInfo[3]).encode("utf-8")
		print "~"*20
		mailTopics.append(repr(mailInfo[3]).encode("utf-8"))
		#mailSums.append(mailInfo[6])
		#mailSources.append(mailInfo[7])
		#Topic="<a href='"+mailInfo[4]+"'>"+unicode(mailInfo[3])+"</a>"
		#htmls.append("Topic:"+Topic+"<hr>Source:"+unicode(mailSources)+"<hr>Summary:"+unicode(mailSums))
		#htmls.append(mailTopics)
	#htmlss=[]
	#htmlss=[mail]
	#return (mailTopics,mailSums,mailSources)
	#return unicode(htmls)
	#return htmlss
	#print "#"*50
	print mailTopics
	return mailTopics
"""		
		

def getMailContents ():
	htmltext=u"\u8c37\u6b4c\u4e91\u5b58\u50a8"
	return htmltext	
		
		
	
	
if __name__ == '__main__' :
	
	mailInfo=getMailInfo()
	authInfo = {}
        authInfo['server'] = mailInfo[0]
        authInfo['user'] = mailInfo[1]
        authInfo['password'] = mailInfo[2]
	print authInfo['user'],
	print authInfo['password'],"hahaha"
	#print authInfo['server']
        fromAdd=mailInfo[3]
        #toAdd =str(mailInfo[4])
	toAdd=['kojp@qq.com']
	#print toAdd
	rankOper=mailInfo[5]
	rankValue=mailInfo[6]
        subject =mailInfo[7]
	#htmlText=getMailContents(rankOper,rankValue)
	#print unicode(htmlText).encode('gb2312'),"dddddddddd"*10
	htmlText=getMailContents()
        plainText = 'TXT'
        #htmlText = '<B>HTMLs</B><a href="www.baidu.com">badidu.com</a>'
        #htmlText=unicode(htmlText).encode("gbk")
	#print htmlText
	print "*"*100
	for s in htmlText:
		print "fuckey"
		s=unicode(s)
		print s,"#EEEEEEEEEEEE"
		print isinstance(s,str)
		#s=unicode(s)
		#print isinstance(s,unicode),"ccc"
		#print s,"ddd"
		#print s.decode("gbk").encode("gbk"),"#EEEEEEE"

		#htmlTextutf8=s.encode("utf8")+"<Hr>"
	#sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText)
