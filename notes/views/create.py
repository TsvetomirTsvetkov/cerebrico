# from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django import forms
from notes.models import File

# Parser imports # Needed in the folders
from ..src.preprocessors import KeywordPreprocessor
from ..src.postprocessors import KeywordPostprocessor
from ..src.extensions import Extension
from markdown import Markdown


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = ["upload"]


class TextForm(forms.Form):
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Start writing your notes here")

@login_required
def create(request):
    upload_form = UploadFileForm(request.POST, request.FILES)
    text_form = TextForm(request.POST)
    if request.method == "POST":
        if 'upload_form' in request.POST:
            if upload_form.is_valid():
                # upload_form.save()
                print('Upload form')
            else:
                print('Upload form invalid')

        if 'text_form' in request.POST:
            if text_form.is_valid():
                # TODO: Do something with the form - create file instance
                print('Text form')
            else:
                print('Text form invalid')

    else:
        upload_form = UploadFileForm()
        text_form = TextForm()

    return render(
        request,
        'notes/create.html',
        {
            'text_form': text_form,
            'upload_form': upload_form
        }
    )