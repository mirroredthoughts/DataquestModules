## 3. Psycopg2 ##

import psycopg2 as ps
conn = ps.connect("dbname=dq user=dq")
cur= conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
query= "CREATE TABLE notes(id integer PRIMARY KEY,body text,title text);"
cur=conn.cursor()
cur.execute(query)
conn.close()
     

## 5. SQL Transactions ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
query= "CREATE TABLE notes(id integer PRIMARY KEY,body text,title text);"
cur=conn.cursor()
cur.execute(query)
conn.commit()
conn.close()

## 6. Autocommitting ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
conn.autocommit=True
query= "CREATE TABLE facts(id integer PRIMARY KEY,country text,value integer);"
cur=conn.cursor()
cur.execute(query)
conn.close()

## 7. Executing queries ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
conn.autocommit=True
query= "INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.','Dataquest reminder');"
cur=conn.cursor()
cur.execute(query)
cur.execute("SELECT * FROM notes;")
rows=cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
conn.autocommit=True
query= "CREATE DATABASE income                                                                   OWNER dq;"
cur=conn.cursor()
cur.execute(query)
conn.close()

## 9. Deleting a database ##

import psycopg2 as ps
conn=ps.connect("dbname=dq user=dq")
conn.autocommit=True
query= "DROP DATABASE income;"
cur=conn.cursor()
cur.execute(query)
conn.close()