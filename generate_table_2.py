# -*- coding: cp936 -*-
#this module use SQL to generate table which get from db-book.com
#import MySQLdb

def get_SQL(sql_name):
    #open file and get sql
    #input:sql_name
    #ouput:sql order->str

    sql=""   
    f=open(sql_name,'r')
    sql=f.read()
    f.close()
    
    return sql


"""def generate_talbe_with_SQL():
    #use the sql language get from www.db-book.com
    db=MySQLdb.connect("localhost","root","","testdb")
    coursor=db.cursor


    return
"""
