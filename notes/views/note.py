# External Imports
from markdown import Markdown

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, redirect, render

# Internal Imports
from notes.forms import TextForm, UploadFileForm
from notes.models import File
from notes.src.extensions import KeywordExtension

# Utility functions
def parse_file(file_contents, profile_settings):
    parser = Markdown(extensions=[KeywordExtension(profile_settings=profile_settings)])

    parsed_file = parser.reset().convert(file_contents)

    return parsed_file


# Views
@login_required
def create(request):
    text_form = TextForm(request.POST)
    save_error = False

    if request.method == "POST":
        if text_form.is_valid():
            title = text_form.cleaned_data["title"]
            content = text_form.cleaned_data["content"]
            content_file = ContentFile(name=title, content=content)
            try:
                file = File(user=request.user, title=title, upload=content_file)
                file.save()
                return redirect("notes:note", file)
            except Exception as err:
                print(err)
                text_form = TextForm(request.POST)
                save_error = True
    else:
        text_form = TextForm()

    return render(
        request,
        'notes/create.html',
        {
            'text_form': text_form,
            'save_error': save_error
        }
    )


@login_required
def delete(request, title):
    file = get_object_or_404(request.user.file_set, title=title)
    file.delete()

    return redirect("notes:notes")


@login_required
def edit(request, title):
    file = get_object_or_404(request.user.file_set, title=title)

    with open(file.upload.path, 'r') as f:
        file_content = f.read()

    form = TextForm(initial={'title': file.title, 'content': file_content})

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            try:
                file.title = form["title"].value()
                file.upload.name = form["title"].value()
                # TODO: Actually move file?
                with open(file.upload.path, 'w') as f:
                    f.write(form["content"].value())
                file.save()
                return redirect("notes:note", file.title)
            except Exception:
                formset = TextForm()
    else:
        formset = TextForm()

    return render(
        request,
        'notes/edit.html',
        {
            "file": file,
            "form": form
        }
    )


@login_required
def upload(request):
    upload_form = UploadFileForm(request.POST, request.FILES)

    if request.method == "POST":
        if upload_form.is_valid():
            upload_form.save()
            # TODO: Verify extension / contents

    else:
        upload_form = UploadFileForm()

    return render(
        request,
        'notes/upload.html',
        {
            "upload_form": upload_form
        }
    )


@login_required
def note(request, title):
    file = get_object_or_404(request.user.file_set, title=title)

    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    with open(file.upload.path, 'r') as f:
        file_contents = f.read()

    parsed_file = parse_file(file_contents, profile_settings)

    return render(
        request,
        'notes/note.html',
        {
            "file": file,
            "parsed_file": parsed_file,
            "profile_settings": profile_settings
        }
    )


@login_required
def notes(request):
    files = User.objects.get(username=request.user).file_set.all()

    return render(
        request,
        'notes/notes.html',
        {
            "files": files, 
        }
    )
