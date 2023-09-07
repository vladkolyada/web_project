from django.shortcuts import render
from .models import Client, Message, FeedBack
from .forms import GetContactForm

# Create your views here.


def index(request):
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
    return render(request, "worky/index.html", {
        "form": form,
    })

