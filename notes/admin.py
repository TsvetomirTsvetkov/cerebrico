# External Imports

# Django Imports
from django.contrib import admin

# Internal Imports
from notes.models import Note


# Register Models
admin.site.register(Note)
