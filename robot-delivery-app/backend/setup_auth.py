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
