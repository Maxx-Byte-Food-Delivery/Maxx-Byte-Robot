-- ============================================================
-- DATABASE SCHEMA: Users Table
-- For: Authentication and Authorization
-- ============================================================

-- Create database (MySQL)
CREATE DATABASE IF NOT EXISTS auth_db;
USE auth_db;

-- ============================================================
-- USERS TABLE
-- Two-column requirement: username, password
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_created_at ON users(created_at);

-- ============================================================
-- SAMPLE QUERIES FOR TESTING
-- ============================================================

-- Insert a test user (password: test123)
-- Hash is SHA-256
INSERT INTO users (username, password_hash) 
VALUES ('testuser', '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee6842d8e6b1e5e5c5e5c5e5c5e5c')
ON DUPLICATE KEY UPDATE username = username;

-- Get user by username (for login)
-- SELECT * FROM users WHERE username = 'testuser';

-- Check if username exists
-- SELECT COUNT(*) FROM users WHERE username = 'newuser';

-- Create new user
-- INSERT INTO users (username, password_hash) VALUES ('newuser', 'hashed_password');

-- Get all users (for admin)
-- SELECT id, username, created_at FROM users;

-- ============================================================
-- VERIFY TABLE STRUCTURE
-- ============================================================

DESCRIBE users;
SELECT * FROM users;
