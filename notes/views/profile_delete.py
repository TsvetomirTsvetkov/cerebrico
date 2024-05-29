from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


@login_required
def profile_delete(request):
    request.user.delete()

    return redirect("notes:index")
