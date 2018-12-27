from django import forms
from .models import Post, Contact, FlatPage

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
