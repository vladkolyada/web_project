from django import forms
from .models import Post, Comment


class GetContactForm(forms.Form):
    name = forms.CharField(label="YOUR NAME", min_length=2, max_length=60)
    email = forms.EmailField(label="YOUR EMAIL", min_length=5, max_length=100)
    message = forms.CharField(label="message", widget=forms.Textarea(), min_length=20, max_length=700)


class FormForNewsletterDB(forms.Form):
    email_for_newsletter = forms.EmailField(label="YOUR EMAIL", max_length=100, min_length=5)


class LogInForAdminForm(forms.Form):
    username = forms.CharField(label="YOUR ADMIN USERNAME")
    password = forms.CharField(label="YOUR ADMIN PASSWORD", widget=forms.PasswordInput(attrs={'type': 'password'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "image")


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea())
    email = forms.CharField(min_length=5, max_length=100)
    name = forms.CharField(min_length=2, max_length=60)


class SearchForm(forms.Form):
    search_query = forms.CharField()
