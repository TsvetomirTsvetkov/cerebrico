# External Imports
import os

# Django Imports
from django.core.wsgi import get_wsgi_application

# Internal Imports


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
