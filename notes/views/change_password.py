from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("notes:index")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(
        request,
        'notes/change_password.html',
        {
            'form': form,
        }
    )
