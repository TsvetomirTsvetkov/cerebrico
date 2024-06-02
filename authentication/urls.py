# Django Imports
from django.urls import path

# Internal Imports
from authentication import views


# Define namespace
app_name = 'authentication'

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup")
]
