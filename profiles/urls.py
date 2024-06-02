# Django Imports
from django.urls import path

# Internal Imports
from profiles import views


# Define namespace
app_name = 'profiles'

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/", views.delete, name="delete"),
    path("edit/", views.edit, name="edit"),
    path('edit/change-password/', views.change_password, name='change_password'),
    path("settings/", views.settings, name="settings"),
]
