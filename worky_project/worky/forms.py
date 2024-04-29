from django import forms
from .models import Post, Comment


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


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea())
    email = forms.CharField(max_length=100)
    name = forms.CharField(max_length=60)


class SearchForm(forms.Form):
    search_query = forms.CharField()
