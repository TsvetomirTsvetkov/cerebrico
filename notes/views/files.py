# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def files(request):
    files = User.objects.get(username=request.user).file_set.all()

    return render(
        request,
        'notes/files.html',
        {
            "files": files, 
        }
    )