from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post, Category, MenuItem, Contact


def index(request):
    latest_post_list = Post.objects.filter(post_pinned=False).order_by('-pub_date')
    pinned_post_list = Post.objects.filter(post_pinned=True)
    context = {'latest_post_list': latest_post_list, 'pinned_post_list': pinned_post_list}
    return render(request, 'zsbila/index.html', context)


def clanek(request, nazev):
    urlclanek = Post.objects.get(title_text=nazev)
    context = {'post': urlclanek}
    return render(request, 'zsbila/clanek.html', context)


def kontakty(request):
    # contacts = Contact.objects.get(jmeno=nazev)
    contacts = Contact.objects.filter().order_by('-jmeno')
    context = {'contacts': contacts}
    return render(request, 'zsbila/kontakty.html', context)


def galerie(request):
    # contacts = Contact.objects.get(jmeno=nazev)
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie.html', context)


def galerierocniky(request):
    # contacts = Contact.objects.get(jmeno=nazev)
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-rocniky.html', context)


def galerieakce(request):
    # contacts = Contact.objects.get(jmeno=nazev)
    context = {'galerie': galerie}
    return render(request, 'zsbila/galerie-prehled-akce.html', context)

# Create your views here.
