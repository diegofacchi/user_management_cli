-- Create the database with UTF-8 character set and collation
CREATE DATABASE user_management_cli
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

-- Use the newly created database
USE user_management_cli;

-- Create the 'users' table
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(100) DEFAULT 'N/A',
    password VARCHAR(60) NOT NULL
