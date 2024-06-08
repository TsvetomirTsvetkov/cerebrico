# External Imports
import re

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404

# Internal Imports


# Helper Constants
DONE = "[DONE]"
CHCK = '[CHCK]'
UNCH = '[UNCH]'

# Helper Functions
def update_line(line):
    try:
        if line[:7] != (DONE + " "):
            line = DONE + " " + line
        else:
            line = line[7:]
            print('there', line)
    except Exception as err:
        pass

    return line


def update_note(note, line):
    old_line = line
    new_line = update_line(line)
    
    with open(note.upload.path, 'r') as f:
        note_contents = f.read()

    with open(note.upload.path, 'w') as f:
        note_contents = note_contents.replace(old_line, new_line)
        f.write(note_contents)
        note.save()


# Views
@login_required
def tasks(request):
    notes = User.objects.get(username=request.user).note_set.all()
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    all_tasks_dict = {}

    for note in notes:
        with note.upload.open('r') as f:
            lines = f.readlines()
            for line in lines:
                for item in profile_settings:
                    m = re.search(repr(item), line)
                    if m:
                        if note.title not in all_tasks_dict.keys():
                            all_tasks_dict[note.title] = []

                        split_string = line.split()
                        task_dict = {'state': '', 'item': '', 'text': ''}

                        if split_string[0] == DONE:
                            task_dict['state'] = 'checked'
                            task_dict['item'] = split_string[1]
                            task_dict['text'] = " ".join(split_string[2:])
                        else:
                            task_dict['state'] = ''
                            task_dict['item'] = split_string[0]
                            task_dict['text'] = " ".join(split_string[1:])
                        
                        all_tasks_dict[note.title].append(task_dict)

    if request.method == "POST":
        form_data = request.POST.items()

        for field, value in form_data:
            if '_cb_' in field:
                split_string = field.split('_cb_')
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
