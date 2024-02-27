from django import forms
from .models import Post


class GetContactForm(forms.Form):
    name = forms.CharField(label="YOUR NAME")
    email = forms.EmailField(label="YOUR EMAIL")
    message = forms.CharField(label="message", widget=forms.Textarea())


class FormForNewsletterDB(forms.Form):
    email_for_newsletter = forms.EmailField(label="YOUR EMAIL")


class LogInForAdminForm(forms.Form):
    username = forms.CharField(label="YOUR ADMIN USERNAME")
    password = forms.CharField(label="YOUR ADMIN PASSWORD", widget=forms.PasswordInput(attrs={'type': 'password'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "image")

