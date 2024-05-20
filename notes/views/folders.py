# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from notes.models import File

@login_required
def folders(request):
    files = User.objects.get(username=request.user).file_set.all()

    return render(
        request,
        'notes/folders.html',
        {
            "files": files, 
        }
    )