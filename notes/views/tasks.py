# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def tasks(request):
    return render(
        request,
        'notes/tasks.html',
    )