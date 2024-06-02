# External Imports
import re

# Django Imports
from django.contrib.auth.models import User
from django.shortcuts import render

# Internal Imports


# Views
def search(request):
    found_files = []
    error = None

    query = request.GET.get('q')

    if query:
        if request.user.is_authenticated:
            files = User.objects.get(username=request.user).file_set.all()
            for file in files:
                with open(file.upload.path, 'r') as f:
                    file_contents = f.read()

                if re.search(query, file.title, re.IGNORECASE) or \
                   re.search(query, file_contents, re.IGNORECASE):
                    found_files.append(file)
            if found_files == []:
                error = "Sorry, we couldn't find anything..."
        else:
            error = "Please, sign up or log in if you want to search through your notes."
    else:
        error = "Please, write something first..."

    return render(
        request,
        'notes/search.html',
        {
            "found_files": found_files, 
            "error": error,
        }
    )
