# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from notes.forms import TextForm
from notes.models import File
from django.core.files.base import ContentFile


@login_required
def file_create(request):
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
                return redirect("notes:file", file)
            except:
                text_form = TextForm(request.POST)
                save_error = True
    else:
        text_form = TextForm()

    return render(
        request,
        'notes/file_create.html',
        {
            'text_form': text_form,
            'save_error': save_error
        }
    )