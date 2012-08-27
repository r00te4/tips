#! /usr/bin/python
#coding=utf8
'''
#=============================================================================
#     FileName:		db_create.py
#     Desc:	        MySQLlib to create SQL database and tables, it's used for saving mail message	
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-08-08 09:47:14
#     History:		
#=============================================================================
'''

import getpass, MySQLdb
import logging

class SetupDB:
    def __init__(self, db_host, db_user, db_pass, db_charset, db_unix_socket):
        self.conn = MySQLdb.Connection(db_host, db_user, db_pass, charset = db_charset, unix_socket = db_unix_socket)
        print "Connect Mysql successfully!"
        
    def __del__(self):
        self.conn.close()

    def use_db(self, db_name):
        cur = self.conn.cursor()
        sql_cmd_use = '''use %s''' %db_name
        cur.execute(sql_cmd_use)

    def create_db(self, db_name):
        cur = self.conn.cursor()

        # 创建 mail_db 数据库 
        print "======== create database:  %s ..." %db_name
        sql_cmd_db = '''create database if not exists `%s`''' %db_name
        cur.execute(sql_cmd_db)

        # 选择 mail_db数据库来操作    
        self.use_db(db_name)

        # 创建tb_mail表用来存放uid, from_addr, to_addr, date,等信息, 唯一值uid;
        print "======== create table_mail ..."
        sql_cmd_mail = '''create table if not exists `tb_mail`(
        `id` int unsigned not null auto_increment,
        `uid` varchar(512) not null,
        `from_addr` text null,
        `to_addr` text null,
        `date` text null,
        `subject` text null,
        `text_plain` text null,
        `text_html` text null,
        primary key(`id`)
        ) engine=myisam default charset=utf8;'''
        cur.execute(sql_cmd_mail)
 
        # 创建tb_mail_atta表用来存放附件存放的路径, 附件名称, 唯一值uid;
        print "======== create table_mail_atta ..."
        sql_cmd_mail_atta = '''create table if not exists `tb_mail_atta` (
        `id` int unsigned not null auto_increment,
        `uid` varchar(512) not null,
        `filepath` varchar(512) not null,
        `filename` varchar(512) not null,
        primary key(`id`)
        ) engine=myisam default charset=utf8;'''
        cur.execute(sql_cmd_mail_atta)

    def insert_mail(self, db_name, uid, from_addr, to_addr, date, subject, text_plain, text_html):
        # Mysql特殊字符处理, 把单引号转换成两个单引号
        if from_addr:
            from_addr = from_addr.replace("'", "''")
        if to_addr:
            to_addr = to_addr.replace("'", "''")
        if subject:
            subject = subject.replace("'", "''")
        if text_plain:
            text_plain = text_plain.replace("'","''")
        if text_html:
            text_html = text_html.replace("'","''")
            #text_html = MySQLdb.escape_string(text_html)

        cur = self.conn.cursor()

        # 选择 mail_db数据库来操作    
        self.use_db(db_name)

        # insert一条数据到tb_mail, cursor.execute()可以接受一个参数，也可以接受两个参数, 注意 %s 和 '%s'的区别
        # sql_cmd_insert = "insert into tb_mail(uid, from_addr, to_addr, date, subject, text_plain, text_html) values(%s,%s,%s,%s,%s,%s,%s)"
        print "======== insert mail data to tb_mail table ..."
        param=(uid, from_addr, to_addr, date, subject, text_plain, text_html)
        sql_cmd = "insert into tb_mail(uid, from_addr, to_addr, date, subject, text_plain, text_html) values('%s','%s','%s','%s','%s','%s','%s')" %param
        try:
            cur.execute(sql_cmd)
        except:
            logging.info("uid: %s insert mail message to mysql failed." %uid)
            pass

    def insert_atta(self, db_name, uid, filepath, filename):
        if filepath:
            filepath = filepath.replace("'", "''")
        if filename:
            filename = filename.replace("'", "''")

        cur = self.conn.cursor()
        self.use_db(db_name)

        print "======== insert mail data to tb_mail_atta table ..."
        param=(uid, filepath, filename)
        sql_cmd = "insert into tb_mail_atta(uid, filepath, filename) values('%s','%s','%s')" %param
        try:
            cur.execute(sql_cmd)
        except:
            logging.info("uid: %s insert attachment to mysql failed." %uid)
            pass
    
    def select_uid(self, db_name):
        cur = self.conn.cursor()
        self.use_db(db_name)
        sql_cmd = "select uid from tb_mail"
        cur.execute(sql_cmd)
        return cur.fetchall()

