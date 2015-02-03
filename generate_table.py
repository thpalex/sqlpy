# -*- coding: cp936 -*-
#this module is to generate table
import random

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

def generate_Instructor_table(tableLong):
    #to generate instructor table
    #input:talbe long
    #output:none

    #1.init list
    building_name=[]
    teacher_name=[]
    dept_name=[]
    building_name=get_name('building_name.txt')
    teacher_name=get_name('teacher_name.txt')
    dept_name=get_name('dept_name.txt')

    #2.controled by ID(ID is key in table）,and generate a line data in table
    for i in xrange(1,tableLong+1,1):
        ID=i
        Name=random.choice(teacher_name)
        Dept_name=random.choice(dept_name)
        Salary=int(random.uniform(10000,20000))
        print 'ID: ',ID,' Name: ',Name,' Dept_name: ',Dept_name,' Salary: ',Salary


    return
    
