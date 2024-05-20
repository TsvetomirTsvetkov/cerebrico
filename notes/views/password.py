from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'notes/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')