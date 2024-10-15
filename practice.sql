-- Active: 1728392886748@@127.0.0.1@3306@commercehub



SHOW TABLES
FROM commercehub;

SELECT * 
from commercehub.customers;

ALTER TABLE Customers
DROP COLUMN Email;


CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);

ALTER TABLE Persons
ADD UNIQUE (ID);

SELECT * 
from commercehub.persons;

ALTER TABLE Persons
ADD CONSTRAINT Person UNIQUE (ID,LastName);

SELECT * 
from commercehub.persons;

ALTER TABLE Persons
DROP INDEX Person;

ALTER TABLE Persons
DROP CONSTRAINT UC_Person;