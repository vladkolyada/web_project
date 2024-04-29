import time

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from .models import Client, Message, Newsletter, Admin, Post, Comment, ClientRestFramework
from .forms import GetContactForm, FormForNewsletterDB, PostForm, CommentForm, SearchForm
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .serializers import ClientSerializer

# d = datetime.datetime.now()
# date_t = d.strftime("%d.%m.%Y %H:%M:%S")
# date_d = d.strftime("%d.%m.%Y %H:%M:%S")

# Create your views here.


# class ClientViewSet(generics.ListAPIView):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

class ClientsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClientAPIList(ListCreateAPIView):
    queryset = ClientRestFramework.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = ClientsAPIListPagination


class ClientAPIUpdate(UpdateAPIView):
    queryset = ClientRestFramework.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class ClientAPIDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ClientRestFramework.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class ClientViewSet(APIView):
#     def get(self, request):
#         c = Client.objects.all()
#         return Response({'clients': ClientSerializer(c, many=True).data})
#
#     def post(self, request):
#         serializer = ClientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'client': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Client.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = ClientSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"client": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Client.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         instance.delete()
#         return Response({"client": "delete client" + str(pk)})

# class ClientViewSet(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.ListModelMixin,
#                     GenericViewSet):
#     # queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
#     # @action(methods=['get'], detail=True)
#     # def messages(self, request, pk=None):
#     #     message = Message.objects.get(pk=pk)
#     #     return Response({"message": [m.message for m in message]})
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Client.objects.all()[:3]
#
#         return Client.objects.filter(pk=pk)


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

    search_form = SearchForm(request.POST)
    if request.method == 'POST':
        if 'search_query' in request.POST:
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                return redirect(f'/worky/search/{search_query}')
    else:
        search_form = SearchForm()
    return render(request, "worky/blog.html", {
        'posts': posts,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(posts),
        'search_form': search_form,
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
    recent_posts = Post.objects.all()[::-1][:4]

    search_form = SearchForm(request.POST)
    if request.method == 'POST':
        if 'search_query' in request.POST:
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                return redirect(f'/search/{search_query}')
    else:
        search_form = SearchForm()
    return render(request, "worky/admin_profile.html", {
        'admin': admin,
        'form': search_form,
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
    search_form = SearchForm(request.POST)

    if request.method == "POST":
        if 'comment' and 'email' and 'name' in request.POST:
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
        if 'search_query' in request.POST:
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                return redirect(f'/worky/search/{search_query}')
    else:
        form = CommentForm()
        search_form = SearchForm()

    return render(request, "worky/post.html", context={
        'post': same_post,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(Post.objects.all()[::-1]),
        'form': form,
        'search_form': search_form,
        'comments': comments[::-1],
        'len_comments': len(comments),
    })


def archive(request, month, year):
    posts = Post.objects.all()[::-1]
    archive_posts = []
    recent_posts = posts[:4]
    search_form = SearchForm(request.POST)

    for post_i in posts:
        if post_i.date.month == month and post_i.date.year == year:
            archive_posts.append(post_i)

    if request.method == 'POST':
        if 'search_query' in request.POST:
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                return redirect(f'/worky/search/{search_query}')
    else:
        search_form = SearchForm()
    return render(request, "worky/archive.html", context={
        'posts': archive_posts,
        'month': archive_posts[0].date.strftime("%B"),
        'year': year,
        'search_form': search_form,
        'recent_posts': recent_posts,
        'archive_urls': archive_fun(posts),
    })


def search(request, search_query):
    wanted_posts = []
    if search_query:
        wanted_posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))

    search_form = SearchForm(request.POST)
    if request.method == 'POST':
        if 'search_query' in request.POST:
            if search_form.is_valid():
                search_query = search_form.cleaned_data['search_query']
                return redirect(f'/worky/search/{search_query}')
    else:
        search_form = SearchForm()
    return render(request, "worky/search.html", context={
        'wanted_posts': wanted_posts,
        'search_query': search_query,
        'search_form': search_form,
    })


