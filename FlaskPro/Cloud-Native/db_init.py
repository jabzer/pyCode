#!/usr/bin/python3
import sqlite3, datetime

conn = sqlite3.connect('mydb.db')

cursor = conn.cursor()

drop_table = 'drop table IF EXISTS apirelease'
cursor.execute(drop_table)

drop_table = 'drop table IF EXISTS users'
cursor.execute(drop_table)

conn.commit()

create_table_sql = '''create table IF NOT EXISTS apirelease 
                      (bulidtime data ,version varchar(30) primary key,links varchar2(30),methods varchar2(30) );'''
cursor.execute(create_table_sql)

create_table_sql_1 = '''create table IF NOT EXISTS users 
                      (username varchar2(30),email varchar2(300),password varchar2(30),full_name varchar(30),id integer primary key autoincrement );'''
cursor.execute(create_table_sql_1)

insert_sql = 'insert into apirelease values ("{}","v1","/api/v1/users","get,post,put,delete")'.format(
    datetime.datetime.now())
cursor.execute(insert_sql)

insert_sql = 'insert into users values ("manish","manish@qq.com","pass_manish","manish mai",1)'
cursor.execute(insert_sql)
insert_sql = 'insert into users values ("manish","manish@qq.com","pass_manish","manish mai",2)'
cursor.execute(insert_sql)

conn.commit()

select_sql = 'select * from apirelease'
for row in cursor.execute(select_sql).fetchall():
    print(row)

select_sql = 'select * from users'
for row in cursor.execute(select_sql).fetchall():
    print(row)

cursor.close()
conn.close()
