-- ============================================================
-- SQLITE DATABASE SCHEMA
-- For local development
-- ============================================================

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_created_at ON users(created_at);

-- Insert test user (password: test123)
INSERT OR IGNORE INTO users (username, password_hash) 
VALUES ('testuser', '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee6842d8e6b1e5e5c5e5c5e5c5e5c');

-- Sample queries
-- SELECT * FROM users WHERE username = 'testuser';
-- SELECT COUNT(*) FROM users WHERE username = 'newuser';
-- INSERT INTO users (username, password_hash) VALUES ('newuser', 'hash');
-- SELECT id, username, created_at FROM users;
