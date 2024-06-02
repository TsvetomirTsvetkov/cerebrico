# External Imports

# Django Imports
from django.urls import path

# Internal Imports
from notes import views


# Define namespace
app_name = 'notes'

urlpatterns = [
    path("", views.notes, name="notes"),
    path("create/", views.create, name="create"),
    path("upload/", views.upload, name="upload"),
    path("<str:title>", views.note, name="note"),
    path("<str:title>/delete", views.delete, name="delete"),
    path("<str:title>/edit", views.edit, name="edit"),
]
