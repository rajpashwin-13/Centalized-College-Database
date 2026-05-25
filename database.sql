-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: college_db
-- ------------------------------------------------------
-- Server version	8.0.46

CREATE DATABASE college_db;

USE college_db;

-- =========================
-- DEPARTMENT TABLE
-- =========================

CREATE TABLE department (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(255) NOT NULL

);

INSERT INTO department VALUES
(1, 'CSE'),
(2, 'AIML'),
(3, 'ECE'),
(4, 'Mechanical'),
(5, 'Civil');

-- =========================
-- STUDENT TABLE
-- =========================

CREATE TABLE student (

    student_id INT PRIMARY KEY,

    student_name VARCHAR(255) NOT NULL,

    year INT,

    age INT,

    address VARCHAR(255)

);

INSERT INTO student VALUES
(1, 'Ashwin Raj', 2, 20, 'Kochi'),
(2, 'Thankan', 1, 19, 'Byndoor'),
(3, 'Amritha Nair', 3, 21, 'Kasaragod'),
(4, 'Arjun', 2, 20, 'Kundamkuzhy'),
(5, 'Ashin', 4, 22, 'Kannur');

-- =========================
-- INSTRUCTOR TABLE
-- =========================

CREATE TABLE instructor (

    instructor_id INT PRIMARY KEY,

    instructor_name VARCHAR(255) NOT NULL,

    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES department(department_id)

);

INSERT INTO instructor VALUES
(101, 'Dr. Ravi Kumar', 1),
(102, 'Mrs. Ananya Shetty', 2),
(103, 'Mr. Karthik Rao', 3),
(104, 'Dr. Sneha Nair', 4),
(105, 'Mr. Ajith Menon', 5);

-- =========================
-- COURSES TABLE
-- =========================

CREATE TABLE courses (

    course_id INT PRIMARY KEY,

    course_name VARCHAR(255) NOT NULL,

    department_id INT,

    instructor_id INT,

    course_duration INT,

    FOREIGN KEY (department_id)
    REFERENCES department(department_id),

    FOREIGN KEY (instructor_id)
    REFERENCES instructor(instructor_id)

);

INSERT INTO courses VALUES
(201, 'Database Management System', 1, 101, 6),
(202, 'Artificial Intelligence', 2, 102, 6),
(203, 'Operating Systems', 3, 103, 4),
(204, 'Computer Networks', 4, 104, 5),
(205, 'OOPS With Java', 5, 105, 6),
(206, 'MERN', 2, 104, 6);

-- =========================
-- ENROLLMENT TABLE
-- =========================

CREATE TABLE enrollment (

    student_id INT,

    course_id INT,

    PRIMARY KEY (student_id, course_id),

    FOREIGN KEY (student_id)
    REFERENCES student(student_id),

    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)

);

INSERT INTO enrollment VALUES
(1, 201),
(2, 201),
(1, 202),
(4, 202),
(3, 203),
(5, 205);

-- Dump completed on 2026-05-25 17:53:05
