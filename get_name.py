# -*- coding: cp936 -*-
# codeing=utf8
#��ȡ�������ֿ�ĺ���
def get_name(name):
    #���ļ�����ȡ����name���ڽ���
    namelist=[]
    
    f=open(name,'r')
    source=f.read()
    for str in source.split(','):
        namelist.append(str)

    f.close()
    
    return namelist

