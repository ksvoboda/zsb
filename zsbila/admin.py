from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

from .models import Post, Category, MenuItem, Contact, FlatPage

admin.site.site_header = 'Základní škola Bílá'
admin.site.site_title = 'ZŠ Bílá'
admin.site.index_title = 'Administrace stránek'


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

    def save_model(self, request, obj, form, change):
        obj.post_long_text = obj.post_text.replace("<hr>", "")
        obj.post_short_text = obj.post_text.replace(obj.post_text.split('<hr>')[-1], "").replace("<hr>", "")

        if obj.publisher is None:
            obj.publisher = request.user
        obj.save()

class ContactAdmin(NonSortableParentAdmin):
    model = Contact
    extra = 0


class MenuItemInline(SortableStackedInline):
    model = MenuItem
    extra = 0


class CategoryAdmin(NonSortableParentAdmin):
    inlines = [MenuItemInline]


class FlatPageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

    fieldsets = (
        (None, {'fields': ('url', 'title', 'content',)}),

    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Contact, ContactAdmin)
