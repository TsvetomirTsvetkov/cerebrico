# External Imports

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404

# Internal Imports
from notes.src.preprocessors import KeywordPreprocessor # TODO: Possibly remove from Preprocessor and make common?


# Helper Function
def update_note(note, line):
    old_line = line

    try:
        if line[:6] != "[DONE]":
            line = "[DONE]" + line
        else:
            line = line[6:]
    except Exception as err:
        print(err)
    
    print(old_line)
    print(line)
    print(note.upload.path)
    with open(note.upload.path, 'w+') as f:
        note_contents = ''
        print("######Before")
        print(note_contents)
        note_contents = f.read()
        print("######Reading")
        print(note_contents)
        note_contents.replace(old_line, line)
        print("######Replacing")
        print(note_contents)
        f.write(note_contents)
        print(note_contents)
        note.save()


# Views
@login_required
def tasks(request):
    test = []
    if request.method == "POST":
        checkbutton = ''

        form_data = request.POST.items()
        for field, value in form_data:
            if '_cb_' in field:
                checkbutton += value
                checkbutton = checkbutton.replace('\r', '').replace('\n', '')
                
                note_title = field.split('_cb_')[0]
                
                try:
                    note = get_object_or_404(request.user.note_set, title=note_title)
                    update_note(note, checkbutton)
                except Exception as err:
                    print(err)

                checkbutton = ''
    
    notes = User.objects.get(username=request.user).note_set.all()
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    all_tasks_dict = {}

    for note in notes:
        with note.upload.open('r') as f:
            lines = f.readlines()
            for line in lines:
                m = KeywordPreprocessor.check_for_patterns(line, profile_settings)
                if m:
                    if note.title not in all_tasks_dict.keys():
                        all_tasks_dict[note.title] = []
                    all_tasks_dict[note.title].append(line)

    return render(
        request,
        'notes/tasks.html',
        {
            "note": note, 
            "all_tasks_dict": all_tasks_dict,
            "counter": 0
        }
    )
