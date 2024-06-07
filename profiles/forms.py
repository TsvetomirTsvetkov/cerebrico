# External Imports

# Django Imports
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Internal Imports
from profiles.models import ProfileSettings

# Forms
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

