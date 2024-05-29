# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect

from notes.forms import UserUpdateForm

@login_required
def profile_edit(request):

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='notes:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        'notes/profile_edit.html',
        {
            "form": form
        }
    )