from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("file/<str:title>", views.file, name="file"),
    path("folders/", views.folders, name="folders"),
    path("tasks/", views.tasks, name="tasks"),
    path("board/", views.board, name="board"),
    path("settings/", views.settings, name="settings"),
    path("profile", views.profile, name="profile"),
    path('profile/password-change/', views.ChangePasswordView.as_view(), name='password'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup")
]
