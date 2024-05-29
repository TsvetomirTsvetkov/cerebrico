from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


@login_required
def file_delete(request, title):
    file = get_object_or_404(request.user.file_set, title=title)
    file.delete()

    return redirect("notes:files")
