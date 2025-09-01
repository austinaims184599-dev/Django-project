#!/bin/bash

# Django Deployment Test - Startup Script

echo "🚀 Starting Django Deployment Test..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create sample data
echo "📝 Creating sample data..."
python manage.py create_sample_data

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Setup complete! Starting development server..."
echo "🌐 Visit http://127.0.0.1:8000 to see the application"
echo "📡 API Status: http://127.0.0.1:8000/api/status/"
echo "👤 Admin: http://127.0.0.1:8000/admin/ (create superuser first)"

# Start development server
python manage.py runserver
