from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.contrib.flatpages.models import FlatPage

favicon_view = RedirectView.as_view(url='/static/pictures/zsbila-logo.ico', permanent=True)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clanek/<str:nazev>', views.clanek, name='clanek'),
    path('kontakty', views.kontakty, name='kontakty'),
    url(r'^favicon\.ico$', favicon_view),
]
