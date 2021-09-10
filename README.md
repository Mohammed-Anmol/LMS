# Library-Management-system-using-Python-and-SQL
The Library Management System In Python is a simple project developed using Python as frontend and SQL as backend. This is a simple console-base project which is very easy to understand and use. Also, this project makes it easy for the library to keep the records of books, borrowing and returning of books in a digital way.

Project Prerequisites

tkinter – Please run below command to install tkinter

*pip install tkinter*

pillow – Please run below command to install tkinter


*pip install pillow*

pymysql – Please run below command to install tkinter

*pip install pymysql*

*Note: You are required to have SQL server installed on your system in order to make pymysql work. If you do not have it ready, please download from SQL Official website*

Description of SQL Tables

Create Tables

*create database db;* (password = "password")

*create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));*

*create table books_issued(bid varchar(20) primary key, issuedto varchar(30));*
