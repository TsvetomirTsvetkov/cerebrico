from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("folders/", views.folders, name="folders"),
    path("tasks/", views.tasks, name="tasks"),
    path("board/", views.board, name="board"),
    path("settings/", views.settings, name="settings"),
]
