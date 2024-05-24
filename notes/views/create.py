# from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django import forms


class TextForm(forms.Form):
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Start writing your notes here")

@login_required
def create(request):
    text_form = TextForm(request.POST)
    if request.method == "POST":
        if text_form.is_valid():
            # TODO: Do something with the form - create file instance
            print('Text form')
        else:
            print('Text form invalid')

    else:
        text_form = TextForm()

    return render(
        request,
        'notes/create.html',
        {
            'text_form': text_form,
        }
    )