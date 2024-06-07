# External Imports

# Django Imports
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Internal Imports
from notes.models import Note


# Forms
class TextForm(forms.Form):
    title = forms.CharField(label=_("Title"), max_length=250)
    content = forms.CharField(label=_("Notes"), widget=forms.Textarea)


class UploadNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["upload"]

    def __init__(self, *args, **kwargs):
        super(UploadNoteForm, self).__init__(*args, **kwargs)
        self.fields["upload"].label = _("Upload")
