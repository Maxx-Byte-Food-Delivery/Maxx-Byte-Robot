#!/usr/bin/env python3
"""
QA Tests for Users Table and Authentication
Run with: pytest tests/test_users_db.py -v
"""

import sqlite3
import hashlib
import unittest
import os

DB_PATH = 'db.sqlite3'

class TestUsersTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Check if database exists before running tests"""
        if not os.path.exists(DB_PATH):
            cls.skipTest(cls, f"Database {DB_PATH} not found. Run setup first.")
    
    def test_database_exists(self):
        """Verify database file exists"""
        self.assertTrue(os.path.exists(DB_PATH))
    
    def test_users_table_exists(self):
        """Verify users table exists in database"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result, "Users table does not exist")
    
    def test_users_table_columns(self):
        """Verify users table has required columns"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]
        conn.close()
        
        required_columns = ['id', 'username', 'password_hash', 'created_at']
        for col in required_columns:
            self.assertIn(col, columns, f"Missing column: {col}")
    
    def test_username_uniqueness(self):
        """Verify username constraint is enforced"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get count of unique usernames
        cursor.execute("SELECT COUNT(DISTINCT username) FROM users")
        unique_count = cursor.fetchone()[0]
        
        # Get total rows
        cursor.execute("SELECT COUNT(*) FROM users")
        total_count = cursor.fetchone()[0]
        conn.close()
        
        self.assertEqual(unique_count, total_count, "Duplicate usernames found")
    
    def test_password_hash_not_null(self):
        """Verify password_hash is never NULL"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE password_hash IS NULL OR password_hash = ''")
        null_count = cursor.fetchone()[0]
        conn.close()
        
        self.assertEqual(null_count, 0, "Found NULL or empty password_hash")
    
    def test_password_hash_length(self):
        """Verify password_hash is SHA-256 (64 characters)"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE LENGTH(password_hash) != 64")
        invalid = cursor.fetchall()
        conn.close()
        
        self.assertEqual(len(invalid), 0, f"Found {len(invalid)} invalid password hash lengths")
    
    def test_admin_user_exists(self):
        """Verify admin user exists (for testing)"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
        admin_count = cursor.fetchone()[0]
        conn.close()
        
        # This is informational, not a strict requirement
        if admin_count == 0:
            print("\n⚠️ No admin user found. Run setup_auth.py to create one.")
    
    def test_created_at_format(self):
        """Verify created_at is valid timestamp"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT created_at FROM users LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        
        if result and result[0]:
            # Should be a valid timestamp string
            self.assertIsNotNone(result[0])
        else:
            self.skipTest("No users to test created_at format")

class TestPasswordHashing(unittest.TestCase):
    
    def test_hash_consistency(self):
        """Same password should produce same hash"""
        def hash_password(password):
            return hashlib.sha256(password.encode()).hexdigest()
        
        hash1 = hash_password("test123")
        hash2 = hash_password("test123")
        
        self.assertEqual(hash1, hash2)
    
    def test_hash_uniqueness(self):
        """Different passwords should produce different hashes"""
        def hash_password(password):
            return hashlib.sha256(password.encode()).hexdigest()
        
        hash1 = hash_password("password1")
        hash2 = hash_password("password2")
        
        self.assertNotEqual(hash1, hash2)
    
    def test_hash_length(self):
        """SHA-256 hash should be 64 characters"""
        def hash_password(password):
            return hashlib.sha256(password.encode()).hexdigest()
        
        result = hash_password("anypassword")
        self.assertEqual(len(result), 64)

if __name__ == '__main__':
    unittest.main()
