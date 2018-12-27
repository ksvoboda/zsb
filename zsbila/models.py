from django.db import models
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from django.core.exceptions import ValidationError
from django.contrib.flatpages.models import FlatPage


class Post(models.Model):
    post_pinned = models.BooleanField('Připnutý na vrchu')
    title_text = models.CharField('Nadpis', max_length=200)
    post_text = models.TextField('Text')

    post_short_text = models.TextField(editable=False)
    post_long_text = models.TextField(editable=False)

    pub_date = models.DateTimeField(auto_now=True)
    publisher = models.CharField('Autor', null=True, blank=True, max_length=200, editable=True)

    def __str__(self):
        return self.title_text

    class Meta:
        verbose_name = 'příspěvek'
        verbose_name_plural = 'příspěvky'


class Contact(models.Model):
    jmeno = models.CharField('Jméno', max_length=200)
    email = models.EmailField('Email', max_length=200)
    tridni = models.CharField('Třída', max_length=200, null=True, blank=True)
    predmety = models.CharField('Předměty', max_length=200)

    def __str__(self):
        return self.jmeno

    class Meta:
        verbose_name = 'kontakt'
        verbose_name_plural = 'kontakty'


class Category(models.Model):
    name = models.CharField('Název', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = "menu"


class MenuItem(SortableMixin):
    item_title = models.CharField('Text v menu', max_length=200)
    #item_internal = models.ForeignKey(FlatPage, on_delete=models.CASCADE, verbose_name='vnitřní stránka',
    #                                   help_text='Použijte při odkazování na stránku školy.', blank=True, null=True)
    #item_external = models.CharField("vnější stránka (odkaz)", max_length=500000,
    #                                 help_text='Použijte při odkazování mimo stránky školy.', blank=True, null=True)
    item_category = SortableForeignKey(Category, on_delete=models.CASCADE)
    item_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    item_link = models.CharField(max_length=500000, editable=True)

    def __str__(self):
        return self.item_title

    #def clean(self):
    #    if self.item_external is not None:
    #        raise ValidationError('Položka v menu nemůže odkazovat na vnitřní a vnější stránku zároveň.')
    #    if self.item_external is None:
    #        raise ValidationError('Položka v menu musí odkazovat.')
    #    else:
    #        if self.item_external is not None:
    #            self.item_link = self.item_external
    #        elif self.item_internal is not None:
    #            self.item_link = '/' + self.item_internal.title_text.replace(' ', '%20')

    class Meta:
        verbose_name = 'položka v menu'
        verbose_name_plural = 'položky v menu'
        ordering = ['item_order']
