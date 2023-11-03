from django.shortcuts import render
from django.http import Http404, HttpResponse
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


def services(request):
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
    return render(request, "worky/services.html", {
        "form": form,
        "home": False,
        "about": False,
        "services": True,
        "blog": False,
    })


def blog(request):
    form = GetContactForm()

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            client = Client(name=name, email=email)
            client.save()

            client_message = Message(client=client, message=message)
            client_message.save()
    return render(request, "worky/blog.html", {
        "form": form,
        "home": False,
        "about": False,
        "services": False,
        "blog": True,
    })


