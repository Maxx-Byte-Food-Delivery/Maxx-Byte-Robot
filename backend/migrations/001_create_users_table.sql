-- ============================================================
-- Users Table for Authentication
-- For: Dev Team, Security Team, Data Team
-- ============================================================

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);

-- Insert default admin (password will be set via setup script)
-- No hardcoded passwords in schema
