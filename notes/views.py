from django.http import HttpResponse
from django.shortcuts import render

# TODO: Possibly create a subfolder w/ views and move the file there
def index(request):
    return render(
        request,
        'index.html',
    )
