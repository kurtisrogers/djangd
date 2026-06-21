from django.conf import settings
from django.urls import include, path

from example_app import views

urlpatterns = [
    path("", views.home, name="home"),
]

if settings.DEBUG:
    urlpatterns += [path("pattern-library/", include("pattern_library.urls"))]
