#!/bin/bash

# MAXX BYTE - Create Users Table Script
# Following the backend folder structure

echo "========================================="
echo "MAXX BYTE - CREATE USERS TABLE"
echo "========================================="
echo ""

# Create migrations folder if not exists
mkdir -p migrations

# Create the users table migration file
cat > migrations/001_create_users_table.sql << 'SQL'
-- Create users table for authentication
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default admin user (password: admin123)
INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123');
SQL

echo "✅ Created: migrations/001_create_users_table.sql"

# Create setup script
cat > setup_auth.py << 'PYTHON'
#!/usr/bin/env python3
"""
Setup script for authentication database.
Run this to create the users table.
"""

import sqlite3
import os

DB_PATH = 'db.sqlite3'

def setup_users_table():
    """Create users table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert default admin user
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password) 
        VALUES ('admin', 'admin123')
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Users table created successfully")

if __name__ == '__main__':
    setup_users_table()
PYTHON

echo "✅ Created: setup_auth.py"

# Update requirements.txt if needed
if [ -f "requirements.txt" ]; then
    if ! grep -q "db.sqlite3" requirements.txt; then
        echo "# SQLite is built-in - no additional package needed" >> requirements.txt
    fi
    echo "✅ requirements.txt checked"
fi

# Add to git
echo ""
echo "Adding files to git..."
git add migrations/001_create_users_table.sql
git add setup_auth.py
git status

echo ""
echo "========================================="
echo "NEXT STEPS"
echo "========================================="
echo ""
echo "1. Commit and push:"
echo "   git commit -m 'feat(auth): add users table schema'"
echo "   git push origin user"
echo ""
echo "2. Or run the setup script:"
echo "   python setup_auth.py"
echo ""
