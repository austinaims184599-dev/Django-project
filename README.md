# Django Deployment Test Project

A simple Django project designed specifically for testing deployment scenarios. This project includes a modern web interface, REST API endpoints, and comprehensive deployment configurations for various platforms.

## 🚀 Features

- **Modern Web Interface**: Responsive design with Bootstrap 5 and Font Awesome icons
- **REST API**: Simple API endpoints for testing API functionality
- **Database Models**: Sample Post model with admin interface
- **Docker Support**: Complete containerization setup
- **Production Ready**: Separate production settings and security configurations
- **Multiple Deployment Options**: Docker, Docker Compose, and cloud platform ready

## 📋 Prerequisites

- Python 3.11+
- pip (Python package installer)
- Docker (optional, for containerized deployment)
- PostgreSQL (optional, for production database)

## 🛠️ Local Development Setup

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd Django-project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp env.example .env

# Edit .env file with your settings
# Update SECRET_KEY and other variables as needed
```

### 3. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Load sample data (optional)
python manage.py shell
>>> from main.models import Post
>>> Post.objects.create(title="Welcome Post", content="This is a sample post for testing deployment.")
>>> exit()
```

### 4. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the application.

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Using Docker Only

```bash
# Build the image
docker build -t django-deploy-test .

# Run the container
docker run -p 8000:8000 django-deploy-test
```

## ☁️ Cloud Deployment

### Heroku

1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
4. Deploy: `git push heroku main`

### AWS/GCP/Azure

1. Use the provided Dockerfile for container deployment
2. Configure environment variables for production
3. Set up PostgreSQL database
4. Configure static file serving
5. Set up SSL certificates

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `True` |
| `DB_NAME` | Database name | `deploytest` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `postgres` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `ALLOWED_HOSTS` | Allowed hosts (comma-separated) | `localhost,127.0.0.1` |

### Production Settings

For production deployment, use the production settings:

```bash
# Set Django settings module
export DJANGO_SETTINGS_MODULE=deploytest.settings_production

# Or run with settings
python manage.py runserver --settings=deploytest.settings_production
```

## 📡 API Endpoints

### Status Check
- **GET** `/api/status/` - Returns application status
- **Response**: `{"status": "success", "message": "Django deployment test is working!", "version": "1.0.0"}`

### Posts API
- **GET** `/api/posts/` - Get all posts
- **POST** `/api/posts/` - Create new post
  - **Body**: `{"title": "Post Title", "content": "Post content"}`

## 🧪 Testing Deployment

### Health Checks

1. **Web Interface**: Visit the home page
2. **API Status**: Check `/api/status/`
3. **Database**: Verify posts are loading
4. **Static Files**: Ensure CSS/JS are loading
5. **Admin Interface**: Test `/admin/` (if superuser created)

### Load Testing

```bash
# Install Apache Bench (if available)
ab -n 100 -c 10 http://localhost:8000/

# Or use curl for simple testing
curl http://localhost:8000/api/status/
```

## 📁 Project Structure

```
Django-project/
├── deploytest/           # Main Django project
│   ├── __init__.py
│   ├── settings.py       # Development settings
│   ├── settings_production.py  # Production settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                 # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/            # HTML templates
│   ├── base.html
│   └── main/
│       ├── home.html
│       └── about.html
├── static/              # Static files (CSS, JS, images)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── env.example
└── README.md
```

## 🔒 Security Considerations

- Change the default SECRET_KEY in production
- Set DEBUG=False in production
- Configure ALLOWED_HOSTS properly
- Use HTTPS in production
- Keep dependencies updated
- Use environment variables for sensitive data

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Change port or stop conflicting services
2. **Database connection errors**: Check database configuration
3. **Static files not loading**: Run `python manage.py collectstatic`
4. **Permission errors**: Check file permissions and user settings

### Logs

- Development: Check console output
- Production: Check application logs
- Docker: Use `docker-compose logs`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Review Django documentation
- Create an issue in the repository