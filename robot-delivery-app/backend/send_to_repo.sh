#!/bin/bash

echo "========================================="
echo "Sending User Database Changes to Repo"
echo "========================================="

# Check current branch
BRANCH=$(git branch --show-current)
echo "Current branch: $BRANCH"

# Add all schema and setup files
echo ""
echo "Adding files..."
git add schemas/*.sql
git add setup_user_db.py
git add check_db.py
git add users/models.py
git add users/views.py
git add users/urls.py
git add DEV_TEST_REQUEST.md

# Exclude database file
git reset user_orders.db 2>/dev/null

# Show what's being committed
echo ""
echo "Files to commit:"
git status --short

# Commit
echo ""
echo "Committing changes..."
git commit -m "feat(user): add complete user database with order history

- Added users table (username, email, password_hash, first_name, last_name)
- Added order_history and order_items tables
- Added bcrypt password hashing
- Added Flask API endpoints: /api/users, /api/users/<id>/orders, /api/login
- Added setup_user_db.py for database initialization
- Added check_db.py for verification
- Mock users: john_doe, jane_smith (password: test123)

Test credentials:
- john_doe / test123
- jane_smith / test123
- admin / admin123

Setup: python setup_user_db.py
API: python users/order_api.py"

# Push to remote
echo ""
echo "Pushing to remote..."
git push origin $BRANCH

echo ""
echo "========================================="
echo "✅ Changes sent to repository!"
echo "Branch: $BRANCH"
echo "========================================="
