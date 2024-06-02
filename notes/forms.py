# External Imports

# Django Imports
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# Internal Imports
from notes.models import Note


# Forms
class TextForm(forms.Form):
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Notes", widget=forms.Textarea)


class UploadNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["upload"]
