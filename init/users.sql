create database if not exists userdatabase ;

use userdatabase;

create table users (
    id int AUTO_INCREMENT PRIMARY KEY, 
    fullname varchar(30) NOT NULL, 
    email_id  varchar(100) unique, 
    gender  varchar(10), 
    dob date, 
    created_date date 

);