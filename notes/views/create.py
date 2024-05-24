# from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from notes.forms import TextForm


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