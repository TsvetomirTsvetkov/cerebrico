# External Imports

# Django Imports
from django.contrib.auth.models import User
from django.forms import ModelForm

# Internal Imports


# Forms
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

