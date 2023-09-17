from django.shortcuts import render
from .models import Client, Message, FeedBack
from .forms import GetContactForm

# Create your views here.


def home(request):
    form = GetContactForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            client = Client(name=name, email=email)
            client.save()

            client_message = Message(client=client, message=message)
            client_message.save()
    return render(request, "worky/home.html", {
        "form": form,
        "home": True,
        "about": False,
        "services": False,
        "blog": False,
    })


def about(request):
    form = GetContactForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            client = Client(name=name, email=email)
            client.save()

            client_message = Message(client=client, message=message)
            client_message.save()
    return render(request, "worky/about.html", {
        "form": form,
        "home": False,
        "about": True,
        "services": False,
        "blog": False,
    })

