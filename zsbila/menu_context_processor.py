from .models import Category, MenuItem


def menu_processing(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    context = {'categories': categories, 'items': items}
    return context
