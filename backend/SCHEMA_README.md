# Database Schema Documentation

## Users Table

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Unique login name |
| password_hash | TEXT | SHA-256 hashed password |
| created_at | TIMESTAMP | Account creation time |

## For Dev Team
- Use `setup_auth.py` to initialize the database
- Connect using: `sqlite3 db.sqlite3`

## For Security Team
- Passwords are hashed using SHA-256
- No plaintext passwords stored
- Admin password set via interactive prompt (not in code)

## For Data Team
- Username is unique index for fast lookups
- Created_at enables time-based analytics
