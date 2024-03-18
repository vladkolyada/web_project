from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import Client, Message, Newsletter, Admin, Post, Comment
from .forms import GetContactForm, FormForNewsletterDB, LogInForAdminForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
import datetime

d = datetime.datetime.now()
# date_t = d.strftime("%d.%m.%Y %H:%M:%S")
# date_d = d.strftime("%d.%m.%Y %H:%M:%S")

# Create your views here.


def archive_fun(db):
    archive_urls = []
    for post_i in db:
        if archive_urls.count({'all': f"{post_i.date.strftime('%B %Y')}", 'year': f"{post_i.date.year}",
                               'month': f"{post_i.date.month}"}) < 1:
            new_item = {'all': f"{post_i.date.strftime('%B %Y')}",
                        'year': f"{post_i.date.year}",
                        'month': f"{post_i.date.month}"}
            archive_urls.append(new_item)
    return archive_urls


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
    posts = Post.objects.all()[::-1]
    recent_posts = posts[:4]
    return render(request, "worky/blog.html", {
        'posts': posts,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(posts),
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
    return render(request, "worky/log_in_admin.html", {
            })


def admin_profile(request, admin_username):
    admin = Admin.objects.get(username=admin_username)
    posts = Post.objects.filter(author=admin)[::-1]
    recent_posts = posts[:4]

    return render(request, "worky/admin_profile.html", {
        'admin': admin,
        'posts': posts,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(posts),
    })


@login_required(login_url="/worky/log_in_admin")
def create_post(request):
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


def post(request, post_id):
    same_post = Post.objects.filter(id=post_id)[0]
    recent_posts = Post.objects.all()[::-1][:4]
    comments = Comment.objects.filter(post=same_post)

    form = CommentForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            comment = form.cleaned_data["comment"]

            client_filtering = Client.objects.filter(email=email).first()

            if client_filtering:
                client = client_filtering
            else:
                client = Client(name=name, email=email)
                client.save()

            client_comment = Comment(client=client, post=same_post, comment=comment)
            client_comment.save()

    return render(request, "worky/post.html", context={
        'post': same_post,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(Post.objects.all()[::-1]),
        'form': form,
        'comments': comments[::-1],
        'len_comments': len(comments),
    })


def archive(request, month, year):
    posts = Post.objects.all()[::-1]
    archive_posts = []
    recent_posts = posts[:4]
    for post_i in posts:
        if post_i.date.month == month and post_i.date.year == year:
            archive_posts.append(post_i)

    return render(request, "worky/archive.html", context={
        'archive': archive_posts,
        'month': posts[0].date.strftime("%B"),
        'year': year,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(posts),
    })
