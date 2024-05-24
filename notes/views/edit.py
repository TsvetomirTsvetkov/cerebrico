from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import redirect

from notes.forms import TextForm


@login_required
def edit(request, title):
    file = User.objects.get(username=request.user).file_set.get(title=title)

    with open(file.upload.path, 'r') as f:
        file_content = f.read()

    form = TextForm(initial={'title': file.title, 'content': file_content})

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            file.title = form["title"].value()
            with open(file.upload.path, 'w') as f:
                f.write(form["content"].value())
            file.save()
            return redirect("notes:file", file)
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