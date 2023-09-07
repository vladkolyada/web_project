from django import forms


class GetContactForm(forms.Form):
    name = forms.CharField(label="YOUR NAME")
    email = forms.EmailField(label="YOUR EMAIL")
    message = forms.CharField(label="message", widget=forms.Textarea())


