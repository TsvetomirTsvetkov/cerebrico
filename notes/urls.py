from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path("", views.index, name="index"),
    path("files/", views.files, name="files"),
    path("files/create/", views.file_create, name="file_create"),
    path("files/upload/", views.file_upload, name="file_upload"),
    path("files/<str:title>", views.file, name="file"),
    path("files/<str:title>/delete", views.file_delete, name="file_delete"),
    path("files/<str:title>/edit", views.file_edit, name="file_edit"),
    path("tasks/", views.tasks, name="tasks"),
    path("board/", views.board, name="board"),
    path("settings/", views.settings, name="settings"),
    path("profile", views.profile, name="profile"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
    path("profile/delete", views.profile_delete, name="profile_delete"),
    path('profile/edit/change-password/', views.change_password, name='change_password'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup")
]
