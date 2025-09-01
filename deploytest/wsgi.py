"""
WSGI config for deploytest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys
project_path = '/home/austinaims/sites/Django-project'
if project_path not in sys.path:
    sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django-project.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()