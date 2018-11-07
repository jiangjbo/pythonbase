#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("172.16.106.24", "aa", "aa", "aa", 3399, charset='utf8')
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
