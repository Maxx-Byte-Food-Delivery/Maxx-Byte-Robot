import sqlite3

conn = sqlite3.connect('user_orders.db')
cursor = conn.cursor()

print("=== TABLES ===")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for row in cursor.fetchall():
    print(f"  {row[0]}")

print("\n=== USERS ===")
cursor.execute("SELECT id, username, email, first_name, last_name FROM users")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n=== ORDERS ===")
cursor.execute("SELECT order_id, user_id, total_amount, status FROM order_history")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()
