# External Imports

# Django Imports
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

# Internal Imports
from notes.views import index, search, tasks


# Language  URLs
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

# Admin URLs
urlpatterns += [
    path('admin/', admin.site.urls)
]

# User URLs
urlpatterns += i18n_patterns(
    path("", include("authentication.urls")),
    path("", index, name='index'),
    path("search/", search, name='search'),
    path("tasks/", tasks, name='tasks'),
    path('notes/', include('notes.urls')),
    path('profile/', include("profiles.urls")),
    prefix_default_language=True
)
