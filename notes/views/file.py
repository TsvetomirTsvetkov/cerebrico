# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def file(request, title):
    file = User.objects.get(username=request.user).file_set.get(title=title)

    # TODO: Do some magic while parsing and show to user

    return render(
        request,
        'notes/file.html',
        {
            "file": file
        }
    )