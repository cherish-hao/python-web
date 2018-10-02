#!/usr/bin/env python3
#coding=utf-8

import pymysql

conn = pymysql.connect(host="localhost",user="wanghao", \
                   password="123456",db="web",port=3306,charset="utf8")
cur = conn.cursor()
