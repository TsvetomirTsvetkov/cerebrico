from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from notes.models import UserSettings


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, label_suffix=":")

        if form.is_valid():
            user = form.save()
            UserSettings.objects.create(
                user_id=user.id,
                option="To Do",
                keyword="TODO",
                separator=":" 
            )
            login(request, user)
            return redirect('notes:index')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/signup.html',
        {
            'form': form
        }
    )
