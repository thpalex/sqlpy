# -*- coding: cp936 -*-
#this module use SQL to generate table which get from db-book.com
import MySQLdb

def insert_value_with_SQL(sql_name):
    #use the sql to insert data
    db=MySQLdb.connect('localhost','root','','testdb')
    cursor=db.cursor()
    
    f=open(sql_name,'r')
    for line in f:
        try:
            cursor.execute(line)
            db.commit()
        except:
            print "wrong"
            db.rollback()
            continue

    f.close()
    db.close()
            
    
    return

def create_talbe_with_SQL():
    #use the sql to create tables
    db=MySQLdb.connect("localhost","root","","testdb")
    cursor=db.cursor()

    sql_classroom="""
create table classroom
	(building		varchar(15),
	 room_number		varchar(7),
	 capacity		numeric(4,0),
	 primary key (building, room_number)
	);
"""
    sql_departmen="""
create table department
	(dept_name		varchar(20), 
	 building		varchar(15), 
	 budget		        numeric(12,2) check (budget > 0),
	 primary key (dept_name)
	);
"""
    sql_course="""
create table course
	(course_id		varchar(8), 
	 title			varchar(50), 
	 dept_name		varchar(20),
	 credits		numeric(2,0) check (credits > 0),
	 primary key (course_id)
	);
"""
    sql_instructor="""
create table instructor
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 dept_name		varchar(20), 
	 salary			numeric(8,2) check (salary > 29000),
	 primary key (ID)
	);
"""
    sql_section="""
create table section
	(course_id		varchar(8), 
         sec_id			varchar(8),
	 semester		varchar(6)
		check (semester in ('Fall', 'Winter', 'Spring', 'Summer')), 
	 year			numeric(4,0) check (year > 1701 and year < 2100), 
	 building		varchar(15),
	 room_number		varchar(7),
	 time_slot_id		varchar(4),
	 primary key (course_id, sec_id, semester, year)
	);
"""
    sql_teaches="""
create table teaches
	(ID			varchar(5), 
	 course_id		varchar(8),
	 sec_id			varchar(8), 
	 semester		varchar(6),
	 year			numeric(4,0),
	 primary key (ID, course_id, sec_id, semester, year)
	);
"""
    sql_student="""
create table student
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 dept_name		varchar(20), 
	 tot_cred		numeric(3,0) check (tot_cred >= 0),
	 primary key (ID)
	);
"""
    sql_takes="""
create table takes
	(ID			varchar(5), 
	 course_id		varchar(8),
	 sec_id			varchar(8), 
	 semester		varchar(6),
	 year			numeric(4,0),
	 grade		        varchar(2),
	 primary key (ID, course_id, sec_id, semester, year)
	);
"""
    sql_advisor="""
create table advisor
	(s_ID			varchar(5),
	 i_ID			varchar(5),
	 primary key (s_ID)
	);
"""
    sql_time_slot="""
create table time_slot
	(time_slot_id		varchar(4),
	 day			varchar(1),
	 start_hr		numeric(2) check (start_hr >= 0 and start_hr < 24),
	 start_min		numeric(2) check (start_min >= 0 and start_min < 60),
	 end_hr			numeric(2) check (end_hr >= 0 and end_hr < 24),
	 end_min		numeric(2) check (end_min >= 0 and end_min < 60),
	 primary key (time_slot_id, day, start_hr, start_min)
	);
"""
    sql_prereq="""
create table prereq
	(course_id		varchar(8), 
	 prereq_id		varchar(8),
	 primary key (course_id, prereq_id)
	);
"""
    
    cursor.execute(sql_classroom)
    cursor.execute(sql_departmen)
    cursor.execute(sql_course)
    cursor.execute(sql_instructor)
    cursor.execute(sql_section)
    cursor.execute(sql_teaches)
    cursor.execute(sql_time_slot)
    cursor.execute(sql_student)
    cursor.execute(sql_prereq)
    cursor.execute(sql_advisor)
    cursor.execute(sql_takes)
    db.commit()
    
    db.close()

    return

