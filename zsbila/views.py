from django.shortcuts import render

from .models import Post, Category, MenuItem


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
    context = {'contacts': kontakty}
    return render(request, 'zsbila/kontakty.html', context)

# Create your views here.
