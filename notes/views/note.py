# External Imports
from markdown import Markdown

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, redirect, render

# Internal Imports
from notes.forms import TextForm, UploadNoteForm
from notes.models import Note
from notes.src.extensions import KeywordExtension


# Utility functions
def parse_note(note_contents, profile_settings):
    parser = Markdown(extensions=[KeywordExtension(profile_settings=profile_settings)])

    parsed_note = parser.reset().convert(note_contents)

    return parsed_note


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
                note = Note(user=request.user, title=title, upload=content_file)
                note.save()
                return redirect("notes:note", note)
            except Exception as err:
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
    note = get_object_or_404(request.user.note_set, title=title)
    note.delete()

    return redirect("notes:notes")


@login_required
def edit(request, title):
    note = get_object_or_404(request.user.note_set, title=title)

    with open(note.upload.path, 'r') as f:
        note_content = f.read()

    form = TextForm(initial={'title': note.title, 'content': note_content})

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            try:
                note.title = form["title"].value()
                with open(note.upload.path, 'w') as f:
                    f.write(form["content"].value())
                    note.save()
                return redirect("notes:note", note.title)
            except Exception:
                formset = TextForm()
    else:
        formset = TextForm()

    return render(
        request,
        'notes/edit.html',
        {
            "note": note,
            "form": form
        }
    )


@login_required
def upload(request):
    upload_form = UploadNoteForm(request.POST, request.FILES)

    if request.method == "POST":
        if upload_form.is_valid():
            upload_form.save()
    else:
        upload_form = UploadNoteForm()

    return render(
        request,
        'notes/upload.html',
        {
            "upload_form": upload_form
        }
    )


@login_required
def note(request, title):
    get_note = get_object_or_404(request.user.note_set, title=title)
    profile_settings = User.objects.get(username=request.user).profilesettings_set.all()

    with open(get_note.upload.path, 'r') as f:
        note_contents = f.read()

    parsed_note = parse_note(note_contents, profile_settings)

    return render(
        request,
        'notes/note.html',
        {
            "note": get_note,
            "parsed_note": parsed_note,
            "profile_settings": profile_settings
        }
    )


@login_required
def notes(request):
    get_notes = User.objects.get(username=request.user).note_set.all()

    return render(
        request,
        'notes/notes.html',
        {
            "notes": get_notes, 
        }
    )
