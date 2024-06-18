# External Imports
import os

# Django Imports
from django.core.asgi import get_asgi_application

# Internal Imports


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
