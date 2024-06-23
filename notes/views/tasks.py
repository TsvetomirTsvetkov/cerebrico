# External Imports

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Internal Imports
from notes.utils import get_tasks, update_tasks_status


# Views
@login_required
def tasks(request):
    notes = User.objects.get(username=request.user).note_set.all()
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    all_tasks_dict = get_tasks(notes, profile_settings)

    if request.method == "POST":
        form_data = request.POST.items()
        update_tasks_status(request, form_data, all_tasks_dict)

    return render(
        request,
        'notes/tasks.html',
        {
            "all_tasks_dict": all_tasks_dict,
        }
    )
