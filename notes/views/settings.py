# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notes.models import UserSettings

from django.forms import inlineformset_factory
from django.shortcuts import redirect


@login_required
def settings(request):
    UserSettingsFormSet = inlineformset_factory(
        User, 
        UserSettings, 
        fields=["option", "type", "keyword", "separator", "is_prefix"], 
        extra=1
    )

    if request.method == "POST":
        formset = UserSettingsFormSet(request.POST, instance=request.user)
        if formset.is_valid():
            formset.save()
            return redirect("notes:index")
    else:
        formset = UserSettingsFormSet(instance=request.user)

    return render(
        request,
        'notes/settings.html',
        {
            "formset": formset
        }
    )
