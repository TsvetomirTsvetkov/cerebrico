# External Imports

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Internal Imports
from notes.src.preprocessors import KeywordPreprocessor # TODO: Possibly remove from Preprocessor and make common?


# Helper Function
def update_file(file, line):
    old_line = line

    try:
        if line[:6] != "[DONE]":
            line = "[DONE]" + line
        else:
            line = line[6:]
    except:
        # TODO: Possibly handle this
        pass

    with open(file.upload.path, 'rw') as f:
        file_contents = f.read()
        file_contents.replace(old_line, line)
        f.write(file_contents)


# Views
@login_required
def tasks(request):
    files = User.objects.get(username=request.user).file_set.all()
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    all_tasks_dict = {}

    for file in files:
        with file.upload.open('r') as f:
            lines = f.readlines()
            for line in lines:
                m = KeywordPreprocessor.check_for_patterns(line, profile_settings)
                if m:
                    if file.title not in all_tasks_dict.keys():
                        all_tasks_dict[file.title] = []
                    all_tasks_dict[file.title].append(line)

    return render(
        request,
        'notes/tasks.html',
        {
            "files": files, 
            "all_tasks_dict": all_tasks_dict
        }
    )
