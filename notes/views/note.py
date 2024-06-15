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
from notes.utils import CHCK, DONE, UNCH, KeywordTypes, get_tasks, parse_lines, update_note


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

    all_tasks_dict = get_tasks([get_note], profile_settings)

    with open(get_note.upload.path, 'r') as f:
        lines = f.read()

    parsed_note = parse_lines(lines, profile_settings)

    # TODO: Create a common function 
    if request.method == "POST":
        form_data = request.POST.items()

        for field, value in form_data:
            if KeywordTypes.CB in field:
                split_string = field.split(KeywordTypes.CB)
                note_title = split_string[0]
                line = split_string[1]
                
                # TODO: Cleanup from parsed 
                # parsed_note = parsed_note.replace(line, "")
                
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
        'notes/note.html',
        {
            "note": get_note,
            "parsed_note": parsed_note,
            "profile_settings": profile_settings,
            "all_tasks_dict": all_tasks_dict
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
