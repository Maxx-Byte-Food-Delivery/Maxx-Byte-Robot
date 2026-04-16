#!/bin/bash

# MAXX BYTE - Backend Setup Script
# Run this to set up the Django backend environment

echo "========================================="
echo "🤖 RoboEats - Backend Setup"
echo "========================================="
echo ""

# Navigate to backend directory
cd robot-delivery-app/backend

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/Scripts/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Copy environment config file
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env 2>/dev/null || echo "Warning: .env.example not found"
else
    echo "✅ .env file already exists"
fi

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create superuser
echo "👤 Creating superuser..."
python manage.py createsuperuser

# Run server
echo ""
echo "========================================="
echo "🚀 Starting Django server with Daphne..."
echo "========================================="
echo ""
echo "Backend will be available at: http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run with Daphne (ASGI for WebSocket support)
daphne -p 8000 config.asgi:application

