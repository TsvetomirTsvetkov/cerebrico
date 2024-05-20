# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

@login_required
def profile(request):

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            # return redirect(to='profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        'notes/profile.html',
        {
            "form": form
        }
    )