# External Imports

# Django Imports
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

# Internal Imports
from profiles.forms import ProfileUpdateForm 
from profiles.models import ProfileSettings
from profiles.utils import toggle_editable


# Views
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(
        request,
        'profiles/change_password.html',
        {
            'form': form,
        }
    )


@login_required
def delete(request):
    request.user.delete()

    return redirect("index")


@login_required
def edit(request):

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(to='profiles:index')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(
        request,
        'profiles/edit.html',
        {
            "form": form
        }
    )


@login_required
def index(request):
    form = toggle_editable(ProfileUpdateForm(instance=request.user), disabled=True)

    return render(
        request,
        'profiles/index.html',
        {
            "form": form,
        }
    )


@login_required
def settings(request):
    no_errors = True

    labels = {
        'option': _('Option'), 
        'type': _('Type'), 
        'keyword': _('Keyword'), 
        'separator': _('Separator'), 
        'is_prefix': _('Is prefix'), 
        'delete': _('Delete')
    }

    ProfileSettingsFormSet = inlineformset_factory(
        User, 
        ProfileSettings, 
        fields=["option", "type", "keyword", "separator", "is_prefix"], 
        labels=labels,
        extra=1
    )

    if request.method == "POST":
        formset = ProfileSettingsFormSet(request.POST, instance=request.user)
        if formset.is_valid():
            for form in formset:
                keyword = form.cleaned_data.get('keyword')
                separator = form.cleaned_data.get('separator')
                prefix = form.cleaned_data.get('prefix')
                
                item = str(separator) + str(keyword) if prefix else str(keyword) + str(separator)

                if item == '[DONE]':
                    form.add_error('keyword', _("You cannot use this combination of keyword and separator as it's reserved."))
                    no_errors = False
            if no_errors:
                formset.save()
                return redirect("index")
    else:
        formset = ProfileSettingsFormSet(instance=request.user)

    return render(
        request,
        'profiles/settings.html',
        {
            "formset": formset,
            'no_errors': no_errors
        }
    )
