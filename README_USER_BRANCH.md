# User Branch - Database Schema

## Database Structure
- users table with id, username, password_hash, created_at
- Passwords hashed with SHA-256
- Unique constraint on username

## Setup
python setup_auth.py

## Query Examples
sqlite3 db.sqlite3
SELECT * FROM users;
SELECT username FROM users WHERE id = 1;
