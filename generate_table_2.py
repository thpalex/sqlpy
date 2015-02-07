# -*- coding: cp936 -*-
#this module is to generate table
import random
import MySQLdb

def get_name(name):
    #open file and get data
    #input:name
    #ouput:datalist

    
    namelist=[]    
    f=open(name,'r')
    source=f.read()
    for str in source.split(','):
        namelist.append(str)

    f.close()
    
    return namelist


def generate_talbe_with_SQL():
    #use the sql language get from www.db-book.com
    


    return
