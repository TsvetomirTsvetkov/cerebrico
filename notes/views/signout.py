from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def signout(request):
    logout(request)

    return redirect('notes:index')
