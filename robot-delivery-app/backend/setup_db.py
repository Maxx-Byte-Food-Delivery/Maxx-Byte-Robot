import mysql.connector
import os

def setup_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Add your password if set
            database='auth_db'
        )
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(150) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert default admin
        cursor.execute('''
            INSERT IGNORE INTO users (username, password) VALUES ('admin', 'admin123')
        ''')
        
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Database setup complete")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    setup_database()
