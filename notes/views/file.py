from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Parser imports
from markdown import Markdown

from notes.src.extensions import KeywordExtension


def parse_file(file_contents, user_settings):
    parser = Markdown(extensions=[KeywordExtension(user_settings=user_settings)])

    parsed_file = parser.reset().convert(file_contents)

    return parsed_file


@login_required
def file(request, title):
    file = User.objects.get(username=request.user).file_set.get(title=title)

    user_settings = User.objects.get(username=request.user).usersettings_set.all()

    with open(file.upload.path, 'r') as f:
        file_contents = f.read()

    parsed_file = parse_file(file_contents, user_settings)

    return render(
        request,
        'notes/file.html',
        {
            "file": file,
            "parsed_file": parsed_file,
            "user_settings": user_settings
        }
    )