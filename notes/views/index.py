# External Imports
import random

# Django Imports
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Internal Imports


# Helper Constants
TIPS = [
    _("Go to the \"Settings\" tab on the left and customize your keywords."),
    _("You can see all of your tasks in one place. They're in the \"Tasks\" section."),
    _("Click on the folder icon on the left and you\'ll see all of your notes."),
    _("If you want to change your username, password or other profile information, click on \"My profile\" at the top.")
]

QUOTES = [
    _("Well you know, for my experience, your head's for having ideas, not for holding them."),
    _("Write down the thoughts of the moment. Those that come unsought for are commonly the most valuable.")
]

AUTHORS = [
    _("David Allen"),
    _("Francis Bacon"),
]


# Views
def index(request):
    tip_id = random.randint(0, len(TIPS) - 1)
    quote_author_id = random.randint(0, len(QUOTES) - 1)

    return render(
        request,
        'notes/index.html',
        {
            "tip": TIPS[tip_id],
            "quote": QUOTES[quote_author_id],
            "author": AUTHORS[quote_author_id]
        }
    )
