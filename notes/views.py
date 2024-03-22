# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'notes/index.html',
    )

def create(request):
    return render(
        request,
        'notes/create.html',
    )

def folders(request):
    return render(
        request,
        'notes/folders.html',
    )

def tasks(request):
    return render(
        request,
        'notes/tasks.html',
    )

def board(request):
    return render(
        request,
        'notes/board.html',
    )

def settings(request):
    return render(
        request,
        'notes/settings.html',
    )