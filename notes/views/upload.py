# from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from notes.models import File


class UploadFileForm(ModelForm):
    class Meta:
        model = File
        fields = ["upload"]


@login_required
def upload(request):
    upload_form = UploadFileForm(request.POST, request.FILES)

    if request.method == "POST":
        if upload_form.is_valid():
            # upload_form.save()
            print('Upload form')
            # TODO: Verify extension / contents
        else:
            print('Upload form invalid')

    else:
        upload_form = UploadFileForm()

    return render(
        request,
        'notes/upload.html',
        {
            "upload_form": upload_form
        }
    )