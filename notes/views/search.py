# External Imports
import re

# Django Imports
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Internal Imports


# Views
def search(request):
    found_notes = []
    error = None

    query = request.GET.get('q')

    if query:
        if request.user.is_authenticated:
            notes = User.objects.get(username=request.user).note_set.all()
            for note in notes:
                with open(note.upload.path, 'r') as f:
                    note_contents = f.read()

                if re.search(query, note.title, re.IGNORECASE) or \
                   re.search(query, note_contents, re.IGNORECASE):
                    found_notes.append(note)
            if found_notes == []:
                error = _("Sorry, we couldn't find anything...")
        else:
            error = _("Please, sign up or log in if you want to search through your notes.")
    else:
        error = _("Please, write something first...")

    return render(
        request,
        'notes/search.html',
        {
            "found_notes": found_notes,
            "error": error,
        }
    )
