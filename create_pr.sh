#!/bin/bash

# MAXX BYTE - Create Pull Request Script
# This script helps you create a PR to share your database schema with the group

echo "========================================="
echo "MAXX BYTE - CREATE PULL REQUEST"
echo "========================================="
echo ""

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"

if [ "$CURRENT_BRANCH" != "user" ]; then
    echo "Switching to user branch..."
    git checkout user
fi

# Check remote
echo ""
echo "Checking remotes..."
git remote -v

# Ensure remote is set correctly
REMOTE_URL=$(git remote get-url origin)
if [[ "$REMOTE_URL" != *"setitoff66"* ]]; then
    echo "WARNING: Your remote is not set to your fork."
    echo "Current remote: $REMOTE_URL"
    echo ""
    read -p "Do you want to set remote to your fork? (y/n): " fix_remote
    if [ "$fix_remote" = "y" ]; then
        git remote set-url origin git@github.com:setitoff66/Maxx-Byte-Robot.git
        echo "Remote updated."
    fi
fi

# Push latest changes
echo ""
echo "Pushing latest changes to your fork..."
git push -u origin user

# Check if gh CLI is installed
if command -v gh &> /dev/null; then
    echo ""
    echo "GitHub CLI detected. Creating PR via command line..."
    gh pr create --title "feat(auth): add users table schema for authentication" \
                 --body "## What's Changed
- Added users table schema (id, username, password, created_at)
- Added Python setup script for database initialization
- Added .gitignore to exclude database files

## Files Added
- \`robot-delivery-app/backend/migrations/001_create_users_table.sql\`
- \`robot-delivery-app/backend/setup_db.py\`

## How to Test
1. Run \`python setup_db.py\` to create the users table
2. Connect to MySQL and verify \`auth_db.users\` table exists

## Related Issue
Closes #(issue number)" \
                 --base user \
                 --head setitoff66:user
else
    echo ""
    echo "========================================="
    echo "MANUAL PULL REQUEST INSTRUCTIONS"
    echo "========================================="
    echo ""
    echo "GitHub CLI not installed. Please create PR manually:"
    echo ""
    echo "1. Go to: https://github.com/setitoff66/Maxx-Byte-Robot"
    echo "2. Click 'Pull Request'"
    echo "3. Set base repository: Maxx-Byte-Food-Delivery/Maxx-Byte-Robot"
    echo "4. Set base branch: user (or ask the group which branch to target)"
    echo "5. Set head: setitoff66/user"
    echo "6. Click 'Create Pull Request'"
    echo "7. Add title: feat(auth): add users table schema for authentication"
    echo ""
    echo "PR Description:"
    echo "--------------------------------------------------"
    echo "What's Changed:"
    echo "- Added users table schema (id, username, password, created_at)"
    echo "- Added Python setup script for database initialization"
    echo "- Added .gitignore to exclude database files"
    echo ""
    echo "Files Added:"
    echo "- robot-delivery-app/backend/migrations/001_create_users_table.sql"
    echo "- robot-delivery-app/backend/setup_db.py"
    echo "--------------------------------------------------"
    echo ""
fi

echo ""
echo "========================================="
echo "✅ Complete!"
echo "========================================="
