#!/bin/bash

echo "========================================="
echo "USER BRANCH AUDIT"
echo "========================================="
echo ""

echo "1. CURRENT BRANCH"
git branch --show-current
echo ""

echo "2. RECENT COMMITS"
git log --oneline -3
echo ""

echo "3. CHECK FOR DATABASE FILES"
DB_FILES=$(git ls-tree -r user --name-only | grep "\.db")
if [ -n "$DB_FILES" ]; then
    echo "WARNING: Database files found"
else
    echo "OK: No database files"
fi
echo ""

echo "4. CHECK FOR PYCACHE"
PYCACHE=$(git ls-tree -r user --name-only | grep "__pycache__")
if [ -n "$PYCACHE" ]; then
    echo "WARNING: pycache files found"
else
    echo "OK: No pycache files"
fi
echo ""

echo "5. CHECK FOR .gitignore"
if git ls-tree -r user --name-only | grep -q ".gitignore"; then
    echo "OK: .gitignore present"
else
    echo "MISSING: .gitignore"
fi
echo ""

echo "6. CHECK FOR README"
if git ls-tree -r user --name-only | grep -qi "readme"; then
    echo "OK: README present"
else
    echo "MISSING: README"
fi
echo ""

echo "7. CHECK FOR SCHEMA FILES"
SCHEMA=$(git ls-tree -r user --name-only | grep -E "\.sql")
if [ -n "$SCHEMA" ]; then
    echo "OK: Schema files present"
else
    echo "MISSING: Schema files"
fi
echo ""

echo "8. CHECK FOR SETUP SCRIPT"
if git ls-tree -r user --name-only | grep -q "setup_auth.py"; then
    echo "OK: setup_auth.py present"
else
    echo "MISSING: setup_auth.py"
fi
echo ""

echo "========================================="
echo "AUDIT COMPLETE"
echo "========================================="
