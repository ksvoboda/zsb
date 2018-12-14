from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from .forms import PostForm
from .models import Post, Category, MenuItem, Contact


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


def galerie(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie.html', context)


def galerierocniky(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-rocniky.html', context)


def galerieakce(request):
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-akce.html', context)


@login_required
def admin(request):
    # Stránka pro přihlášení
    return HttpResponseRedirect("posts")


def admin_logout(request):
    # Stránka na odhlašování
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def admin_posts_list(request):
    posts = Post.objects.all()
    return render(request, 'zsbila/adminPostsList.html', {"posts": posts})


@login_required
def post_edit(request, nazev):
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
