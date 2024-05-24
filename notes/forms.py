from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

from notes.models import File


class TextForm(forms.Form):
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Start writing your notes here", widget=forms.Textarea)


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = ["upload"]
