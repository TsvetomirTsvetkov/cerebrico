# External Imports

# Django Imports
from django.contrib import admin

# Internal Imports
from profiles.models import ProfileSettings


# Register Models
admin.site.register(ProfileSettings)
