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

def generate_Instructor_table(teacherNum):
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

    #2. connect to db
    db=MySQLdb.connect("localhost","root","","testdb")
    cursor=db.cursor()
    base="insert into instructor values(%d,'%s','%s',%d)"

    #3.controled by ID(ID is key in table）,and generate a line data in table
    for i in xrange(1,teacherNum+1,1):
        ID=i
        Name=random.choice(teacher_name)
        Dept_name=random.choice(dept_name)
        Salary=int(random.uniform(10000,20000))
        #print ID,' ',Name,' ',Dept_name,' ',Salary
        param=(ID,Name,Dept_name,Salary)
        sql=base % param
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print sql
            db.rollback()
            continue

        
    db.close()
    return

def generate_Department_table():
    #1. init list
    dept_name=[]
    building_name=[]
    dept_name=get_name('dept_name.txt')
    building_name=get_name('building_name.txt')

    #2. connect to db
    db=MySQLdb.connect("localhost","root","","testdb")
    cursor=db.cursor()
    base="insert into department values ('%s','%s',%d)"

    #3. controled by dept_name,and generate a line data in table
    for i in range(len(dept_name)-1):
        Dept_name=dept_name[i]
        Building_name=random.choice(building_name)
        Budget=int(random.uniform(200000,300000))
        #print Dept_name,' ',Building_name,' ',Budget
        param=(Dept_name,Building_name,Budget)
        sql=base % param
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print sql
            db.rollback()
            continue

    db.close()
    return
