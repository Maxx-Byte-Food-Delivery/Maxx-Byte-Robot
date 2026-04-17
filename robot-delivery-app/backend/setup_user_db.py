import sqlite3
import hashlib

DB_PATH = 'user_orders.db'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_history (
            order_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_amount REAL,
            status TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    # Mock users
    users = [
        ('john_doe', 'john@test.com', hash_password('test123'), 'John', 'Doe'),
        ('jane_smith', 'jane@test.com', hash_password('test123'), 'Jane', 'Smith'),
    ]
    
    for user in users:
        cursor.execute('INSERT OR IGNORE INTO users (username, email, password_hash, first_name, last_name) VALUES (?, ?, ?, ?, ?)', user)
    
    conn.commit()
    conn.close()
    print("Database created with mock users")

if __name__ == '__main__':
    setup()
