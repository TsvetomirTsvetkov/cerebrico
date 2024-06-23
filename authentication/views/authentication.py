# External Imports

# Django Imports
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Internal App Imports
from profiles.models import ProfileSettings


# Views
class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def signout(request):
    logout(request)

    return redirect('index')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, label_suffix=":")

        if form.is_valid():
            user = form.save()
            ProfileSettings.objects.create(
                user_id=user.id,
                option="To Do",
                keyword="TODO",
                separator=":"
            )
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/signup.html',
        {
            'form': form
        }
    )
