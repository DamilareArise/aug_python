# DATABASE MANAGMENT SYSTEM
    # 1.  Relational DBMS (SQL - Structured Query language)
    # e.g MySQL, PostgreSQL, MSSQL, ORACLE, SQLLite, MariaDB
    
    # 2. Non Relational DBMS (NoSQL)
    # e.g MongoDB, Firebase 
    
# CRUD -> create, read, update and delete
# Database -> Table (rows & Column) e.g SQI database - Student Table()
    
# Type of SQL Queries
# 1. DDL - Data Definition Language e.g CREATE, ALTER, DROP, TRUNCATE
# 2. DML - Data Manipulation Language e.g  INSERT, UPDATE, DELETE 
# 3. DQL - Data Query Language e.g SELECT

#  Table Relationships
# 1. One to One relationship e.g user and profile table
# 2. One to many e.g user and product table
# 3. many to many e.g order table, user table, product table


import mysql.connector as sql

conn =  sql.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='password',
    database='august_db'   # input this after creating the database
)
conn.autocommit = True
mycursor = conn.cursor()

# query = 'SHOW DATABASES'
# print(list(mycursor))
# query = 'DROP DATABASE august_db'
# query = 'CREATE DATABASE august_db'

# query = '''CREATE TABLE customer_table(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         fullname VARCHAR(50),
#         email VARCHAR(50) UNIQUE,
#         account_no VARCHAR(10) UNIQUE,
#         account_bal DECIMAL(10, 2) DEFAULT 0.0,
#         address VARCHAR(50),
#         date_created DATETIME DEFAULT CURRENT_TIMESTAMP
#     )
#     '''

# query  = 'ALTER TABLE customer_table CHANGE account_bal account_balance DECIMAL(10, 2) DEFAULT 0.0'
# query = "ALTER TABLE customer_table ADD password VARCHAR(50) AFTER email"
# query = "ALTER TABLE customer_table DROP COLUMN address" 

# DML

# query = "INSERT INTO customer_table(fullname, email, password, account_no) VALUES('Arise Damilare', 'dami@gmail.com', '1234', '1234567890')"
# query = "INSERT INTO customer_table(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)"
# values = ('Raji Raji', 'raji@gmail.com', '1234', '0987654321')
# mycursor.execute(query, values)


# query = "UPDATE customer_table SET fullname = %s WHERE id= %s" 
# values = ('Raji Abdulmalik', 2)
# mycursor.execute(query, values)

# query = "DELETE FROM customer_table WHERE id = 1"
# mycursor.execute(query)

# DQL

# query = 'SELECT * FROM customer_table'
# mycursor.execute(query)
# details = mycursor.fetchall()
# print(details)

# query = 'SELECT * FROM customer_table WHERE id=2'
# mycursor.execute(query)
# detail = mycursor.fetchone()
# print(detail[2], detail[3], detail[5])

# query = "SELECT fullname, email, account_no, account_balance  FROM customer_table WHERE id = 2"
# mycursor.execute(query)
# detail = mycursor.fetchone()
# print(detail)

# query = "SELECT fullname, email, account_no, account_balance  FROM customer_table WHERE email = %s AND password = %s"
# email = input('Email: ')
# password = input('Password: ')
# values = (email, password)
# mycursor.execute(query, values)
# detail = mycursor.fetchone()
# if detail:
#     print('Login successful')
# else:
#     print('Invalid email and password')

# %r => endswith r 
# r% => startwith r
# %r% => contains r

# query = "SELECT fullname, email FROM customer_table WHERE fullname LIKE '%abdul%'"
# mycursor.execute(query)
# details = mycursor.fetchall()
# print(details)