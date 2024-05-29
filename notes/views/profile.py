# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect

from notes.forms import UserUpdateForm, toggle_editable

@login_required
def profile(request):
    form = UserUpdateForm(instance=request.user)
    form = toggle_editable(form, disabled=True)

    return render(
        request,
        'notes/profile.html',
        {
            "form": form,
        }
    )