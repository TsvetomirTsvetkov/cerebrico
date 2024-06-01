from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from notes.forms import TextForm


@login_required
def file_edit(request, title):
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
                return redirect("notes:file", file)
            except:
                formset = TextForm()
    else:
        formset = TextForm()

    return render(
        request,
        'notes/file_edit.html',
        {
            "file": file,
            "form": form
        }
    )