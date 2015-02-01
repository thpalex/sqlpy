# -*- coding: cp936 -*-
# codeing=utf8
#获取各种名字库的函数
def get_name(name):
    #打开文件，获取所有name用于解析
    namelist=[]
    
    f=open(name,'r')
    source=f.read()
    for str in source.split(','):
        namelist.append(str)

    f.close()
    
    return namelist

