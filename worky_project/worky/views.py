from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import Client, Message, Newsletter, Admin, Posts
from .forms import GetContactForm, FormForNewsletterDB, LogInForAdminForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    form = GetContactForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            client_filtering = Client.objects.filter(email=email).first()

            if client_filtering:
                client = client_filtering
            else:
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

            client_filtering = Client.objects.filter(email=email).first()

            if client_filtering:
                client = client_filtering
            else:
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
    form2 = FormForNewsletterDB(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            email_for_newsletter = form2.cleaned_data["email_for_newsletter"]

            client_filtering = Client.objects.filter(email=email).first()

            try:
                if client_filtering:
                    client = client_filtering
                else:
                    client = Client(name=name, email=email)
                    client.save()
            except RuntimeWarning:
                pass

            client_message = Message(client=client, message=message)
            client_message.save()

            newsletter = Newsletter(email=email_for_newsletter)
            newsletter.save()
    return render(request, "worky/services.html", {
        "form": form,
        "form2": form2,
        "home": False,
        "about": False,
        "services": True,
        "blog": False,
    })


def blog(request):
    posts = Posts.objects.all()

    return render(request, "worky/blog.html", {
        'posts': posts,
        "home": False,
        "about": False,
        "services": False,
        "blog": True,
    })


def log_in_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(request, username=username, password=password)
        if admin:
            login(request, admin)
            return redirect(f'/worky/create_post')
        else:
            return redirect('/worky/log_in_admin')
    return render(request, "worky/log_in_admin.html")


def log_out_admin(request):
    logout(request)
    return render(request, "users/login.html", {
            })


def admin_profile(request, admin_username):
    admin = Admin.objects.get(username=admin_username)
    posts = Posts.objects.filter(author=admin)

    return render(request, "worky/admin_profile.html", {
        'admin': admin,
        'posts': posts,
    })


@login_required
def create_post(request):
    if not request.user.is_authenticated:
        return redirect("/worky/home")
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            admin = Admin.objects.get(username=request.user.username)
            form.instance.author = admin
            form.save()
            return redirect('admin_profile', admin_username=request.user.username)
    else:
        form = PostForm()
    context = {
        'form': form,
    }

    return render(request, "worky/create_post.html", context=context)


