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
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        formset = UserSettingsFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect("notes:index")
    else:
        formset = UserSettingsFormSet(instance=user)

    return render(
        request,
        'notes/settings.html',
        {
            "formset": formset
        }
    )
