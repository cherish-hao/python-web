#!usr/bin/env python3
#coding=utf-8

from . db import *

def select_table(table,column,condition,value):
    sql = "select "+column+" from "+table+" where "+condition+" = '"+value+"'"
    print (sql)
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_columns(table,column):
    sql = "select "+column+" from "+table
    print (sql)
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
