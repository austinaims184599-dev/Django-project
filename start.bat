@echo off
REM Django Deployment Test - Windows Startup Script

echo 🚀 Starting Django Deployment Test...

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo 🗄️ Running database migrations...
python manage.py migrate

REM Create sample data
echo 📝 Creating sample data...
python manage.py create_sample_data

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo ✅ Setup complete! Starting development server...
echo 🌐 Visit http://127.0.0.1:8000 to see the application
echo 📡 API Status: http://127.0.0.1:8000/api/status/
echo 👤 Admin: http://127.0.0.1:8000/admin/ (create superuser first)

REM Start development server
python manage.py runserver

pause
