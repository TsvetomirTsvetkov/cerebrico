# External Imports
import re

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404

# Internal Imports
from notes.utils import CHCK, DONE, UNCH, KeywordTypes, update_note, get_tasks


# Views
@login_required
def tasks(request):
    notes = User.objects.get(username=request.user).note_set.all()
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    all_tasks_dict = get_tasks(notes, profile_settings)

    # TODO: Create a common function 
    if request.method == "POST":
        form_data = request.POST.items()

        for field, value in form_data:
            if KeywordTypes.CB in field:
                split_string = field.split(KeywordTypes.CB)
                note_title = split_string[0]
                line = split_string[1]
                
                for items in all_tasks_dict[note_title]:
                    if (items['item'] + ' ' + items['text']) == line:
                        try:
                            if value == CHCK:
                                items['state'] = 'checked'
                                note = get_object_or_404(request.user.note_set, title=note_title)
                                update_note(note, line)
                            elif value == UNCH:
                                items['state'] = ''
                                note = get_object_or_404(request.user.note_set, title=note_title)
                                update_note(note, DONE + ' ' + line)
                            else:
                                continue
                        except Exception as err:
                            pass

    return render(
        request,
        'notes/tasks.html',
        {
            "all_tasks_dict": all_tasks_dict,
        }
    )
