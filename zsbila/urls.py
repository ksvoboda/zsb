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
    # admin #
    path('admin/', views.admin, name="přihlášení"),
    path('admin/logout', views.admin_logout, name="odhlášení"),
    path('admin/posts', views.admin_posts_list, name="seznam-bodů"),
    path('clanek/<str:nazev>/edit', views.post_edit, name='post_edit'),
    path('clanek/<str:nazev>/delete', views.admin_post_delete, name="smazání-bodu"),

    path('kontakty', views.kontakty, name='kontakty'),
    path('galerie', views.galerie, name='galerie'),
    path('galerierocniky', views.galerierocniky, name='galerierocniky'),
    path('galerieakce', views.galerieakce, name='galerieakce'),
    url(r'^favicon\.ico$', favicon_view),
]
