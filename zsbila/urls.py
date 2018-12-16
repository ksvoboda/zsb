from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.contrib.flatpages.models import FlatPage

favicon_view = RedirectView.as_view(url='/static/pictures/zsbila-logo.ico', permanent=True)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:nazev>', views.clanek, name='clanek'),
    path('contacts', views.kontakty, name='kontakty'),
    path('galery', views.galerie, name='galerie'),
    path('galery-years', views.galerierocniky, name='galerierocniky'),
    path('galery-events', views.galerieakce, name='galerieakce'),
# admin #
    path('admin/', views.admin, name="přihlášení"),
    path('admin/logout', views.admin_logout, name="odhlášení"),
    path('admin/dashboard', views.admin_dashboard, name="dashboard"),
# admin-posts #
    path('admin/posts', views.admin_posts_list, name="seznam-článků"),
    path('admin/post/<str:nazev>/edit', views.admin_post_edit, name='editování-článku'),
    path('admin/post/<str:nazev>/delete', views.admin_post_delete, name="smazání-článku"),
# admin-contacts #
      #  path('admin/contacts', views.admin_contacts_list, name="seznam-kontaktů"),
      #  path('admin/contact/<str:id>/edit', views.admin.contact_edit, name='editovaní-kontaktu'),
      #  path('admin/contact/<str:id>/delete', views.admin_contact_delete, name="smazání-kontaktu"),
# admin-flatpage #
      #  path('admin/flatpages', views.admin_flatpages_list, name="seznam-statických-stránek"),
      #  path('admin/flatpage/<str:id>/edit', views.admin_flatpage_edit, name='editovaní-statické-stránky'),
      #  path('admin/flatpage/<str:id>/delete', views.admin_flatpage_delete, name="smazání-statické-stránky"),

    url(r'^favicon\.ico$', favicon_view),
]
