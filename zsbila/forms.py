from django import forms
from .models import Post, Contact, FlatPage, Category, MenuItem

class PostForm(forms.ModelForm):
 class Meta:
     model = Post
     fields = '__all__'


class ContactForm(forms.ModelForm):
 class Meta:
     model = Contact
     fields = '__all__'


class FlatPageForm(forms.ModelForm):
 class Meta:
     model = FlatPage
     fields = '__all__'


class MenuCatForm(forms.ModelForm):
 class Meta:
     model = Category
     fields = '__all__'

class MenuItemForm(forms.ModelForm):
 class Meta:
     model = MenuItem
     fields = '__all__'
