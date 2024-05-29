# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# TODO: Possibly remove from Preprocessor and make common
from notes.src.preprocessors import KeywordPreprocessor

@login_required
def tasks(request):
    files = User.objects.get(username=request.user).file_set.all()
    user_settings = User.objects.get(username=request.user).usersettings_set.all()

    all_tasks = []
    
    for file in files:
        with file.upload.open('r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                m = KeywordPreprocessor.check_for_patterns(line, user_settings)

                if m:
                    all_tasks.append(line)

    return render(
        request,
        'notes/tasks.html',
        {
            "files": files, 
            "all_tasks": all_tasks
        }
    )
