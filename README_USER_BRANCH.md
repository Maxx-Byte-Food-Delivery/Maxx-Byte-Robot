# User Branch - Database Schema for Authentication

## Overview
This branch contains the database schema for user authentication with username and password.

## Files Included
- database_schema.sql - MySQL schema for production
- sqlite_schema.sql - SQLite schema for local development
- setup_auth.py - Python script to initialize the database
- SCHEMA_README.md - Detailed schema documentation
- DATABASE_ACCESS.md - How to access and query the database

## Database Structure
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## How to Set Up
Option 1: python setup_auth.py
Option 2: sqlite3 db.sqlite3 < sqlite_schema.sql

## How to Query
sqlite3 db.sqlite3
SELECT * FROM users;
SELECT username FROM users WHERE id = 1;

## Security Notes
- Passwords are hashed using SHA-256
- No hardcoded credentials
- Admin password set via interactive prompt

## Files NOT in Repo
- *.db files (actual database data)
- *.sqlite3 files
- __pycache__/

## Branch Location
git checkout user

## Contact
Data Engineering Team
