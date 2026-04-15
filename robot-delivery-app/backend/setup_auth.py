import sqlite3
import hashlib
import getpass

DB_PATH = 'db.sqlite3'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if admin exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        password = getpass.getpass("Enter admin password: ")
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       ('admin', password_hash))
        print("✅ Admin user created")
    
    conn.commit()
    conn.close()
    print("✅ Users table ready")

if __name__ == '__main__':
    setup()
