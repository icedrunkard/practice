# -*- coding: utf-8 -*-

import os, sys, string
import mysql.connector
#import sys


#reload(sys)
#sys.setdefaultencoding('utf-8')



conn = mysql.connector.connect(host='139.199.226.12', user='root', passwd='123456', db='test')



    # get cursor
cursor = conn.cursor()
    # create table
dropSql='drop table product'
createSql = 'create table if not exists product(Prd_name varchar(128) primary key, Count int(4))'
cursor.execute(dropSql)
cursor.execute(createSql)

    # insert one data
sql = "insert into product(Prd_name, Count) values('%s', %d)" % ("ATG", 200)


cursor.execute(sql)


        # insert some datas
sql = "insert into product(Prd_name, Count) values(%s, %s)"
val = (("PPS", 400), ("暗恋我", 150), ("你好测试1", 25))


cursor.executemany(sql, val)


conn.commit()
        # quary data
sql = "select * from product"
cursor.execute(sql)
alldata = cursor.fetchall()
print alldata
if alldata:
    for rec in alldata:
        print rec[0], rec[1]

cursor.close()
conn.close()



