from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.forms import formset_factory

from .forms import PostForm, ContactForm, FlatPageForm, MenuCatForm, MenuItemForm
from .models import Post, Category, MenuItem, Contact, FlatPage


def index(request):
    posts = Post.objects.filter(post_pinned=False).order_by('-pub_date')
    pinned_post_list = Post.objects.filter(post_pinned=True)

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts' : posts, 'pinned_post_list' : pinned_post_list}
    return render(request, 'zsbila/index.html', context)


def clanek(request, nazev):
    urlclanek = Post.objects.get(title_text=nazev)
    context = {'post': urlclanek}
    return render(request, 'zsbila/clanek.html', context)


def kontakty(request):
    contacts = Contact.objects.filter().order_by('-jmeno')
    context = {'contacts': contacts}
    return render(request, 'zsbila/kontakty.html', context)


def onas(request):
    return render(request, 'zsbila/o-nas.html')


def flatpage(request, nazev2):
    urlflatpage = FlatPage.objects.get(title=nazev2)
    context = {'flatpage': urlflatpage}
    return render(request, 'flatpages/default.html', context)


def galerie(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie.html', context)


def galerierocniky(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-rocniky.html', context)


def galerieakce(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-akce.html', context)

# admin
@login_required
def admin(request):
    # Stránka pro přihlášení
    return HttpResponseRedirect("dashboard")


def admin_logout(request):
    # Stránka na odhlašování
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def admin_dashboard(request):
    return render(request, 'zsbila/admindashboard.html')


@login_required
def admin_menuall(request):
    return render(request, 'zsbila/adminMenuAll.html')


# admin - posts
@login_required
def admin_posts_list(request):
    posts = Post.objects.all()
    return render(request, 'zsbila/adminPostsList.html', {"posts": posts})


@login_required
def admin_post_edit(request, nazev):
    if nazev == "new":
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/posts')
        else:
            form = PostForm()
    else:
        instance = Post.objects.get(title_text=nazev)

        if request.method == 'POST':
            form = PostForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/posts')

        else:
            form = PostForm(instance=instance)

    return render(request, 'zsbila/adminPostEdit.html', {'form': form, 'nazev': nazev})


@login_required
def admin_post_delete(request, nazev):
    # Smazání bodu
    Post.objects.get(title_text=nazev).delete()
    return HttpResponseRedirect('/admin/posts')


# admin - contacts
@login_required
def admin_contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'zsbila/adminContactsList.html', {"contacts": contacts})


@login_required
def admin_contact_edit(request, id):
    if id == "new":
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/contacts')
        else:
            form = ContactForm()
    else:
        instance = Contact.objects.get(jmeno=id)

        if request.method == 'POST':
            form = ContactForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/contacts')

        else:
            form = PostForm(instance=instance)

    return render(request, 'zsbila/adminContactEdit.html', {'form': form, 'id': id})


@login_required
def admin_contact_delete(request, id):
    # Smazání bodu
    Contact.objects.get(jmeno=id).delete()
    return HttpResponseRedirect('/admin/contacts')


# admin admin-flatpages
@login_required
def admin_flatpages_list(request):
    flatpages = FlatPage.objects.all()
    return render(request, 'zsbila/adminFlatPagesList.html', {"flatpages": flatpages})


@login_required
def admin_flatpage_edit(request, nazev2):
    if nazev2 == "new":
        if request.method == 'POST':
            form = FlatPageForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/flatpages')
        else:
            form = FlatPageForm()
    else:
        instance = FlatPage.objects.get(title=nazev2)

        if request.method == 'POST':
            form = FlatPageForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/flatpages')

        else:
            form = FlatPageForm(instance=instance)

    return render(request, 'zsbila/adminFlatPageEdit.html', {'form': form, 'nazev2': nazev2})


@login_required
def admin_flatpage_delete(request,nazev2):
    # Smazání bodu
    FlatPage.objects.get(jmeno=id).delete()
    return HttpResponseRedirect('/admin/contacts')

#
#
#
#
# admin - menu category
@login_required
def admin_menu_cat_list(request):
    menu_cat = Category.objects.all()
    return render(request, 'zsbila/adminMenuCatList.html', {"menu_cat": menu_cat})


@login_required
def admin_menu_cat_edit(request, menu_cat):
    if menu_cat == "new":
        if request.method == 'POST':
            form = MenuCatForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/menu-cat')
        else:
            form = MenuCatForm()
    else:
        instance = Category.objects.get(name=menu_cat)

        if request.method == 'POST':
            form = MenuCatForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/menu-cat')

        else:
            form = MenuCatForm(instance=instance)

    return render(request, 'zsbila/adminMenuCatEdit.html', {'form': form, 'menu_cat': menu_cat})


@login_required
def admin_menu_cat_delete(request, menu_cat):
    # Smazání bodu
    Category.objects.get(name=menu_cat).delete()
    return HttpResponseRedirect('/admin/menu-cat')






# admin - menu item
@login_required
def admin_menu_item_list(request):
    menu_item = Category.objects.all()
    return render(request, 'zsbila/adminMenuItemList.html', {"menu_item": menu_item})


@login_required
def admin_menu_item_edit(request, menu_item):
    if menu_item == "new":
        if request.method == 'POST':
            form = MenuItemForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/menu-cat/menu-item')
        else:
            form = MenuItemForm()
    else:
        instance = Category.objects.get(name=menu_item)

        if request.method == 'POST':
            form = MenuItemForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/admin/menu-cat/menu_item')

        else:
            form = MenuItemForm(instance=instance)

    return render(request, 'zsbila/adminMenuItemEdit.html', {'form': form, 'menu_item': menu_item})


@login_required
def admin_menu_item_delete(request, menu_item, item_link):
    # Smazání bodu
    Category.objects.get(name=menu_item).delete()
    return HttpResponseRedirect('/admin/menu-cat/menu_item')
