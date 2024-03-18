import datetime
from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

d = datetime.datetime.now()


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=100, null=False, default="your_email@gmail.com")

    def __str__(self):
        return f"{self.name}({self.email})"


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_message",
                               default=None, null=False)
    message = models.CharField(max_length=700)
    time = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return (f"{self.client} message({self.time}):\n"
                f"{self.message}")


class Newsletter(models.Model):
    email = models.EmailField(max_length=100, null=False, default="some_email@example.com")

    def __str__(self):
        return f"{self.email}"


class Admin(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, null=False, default="admin", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=60, null=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (username: {self.username}, id: {self.id})"


class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    author = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='admin_post', null=False, default=None)
    title = models.CharField(max_length=170, null=False, default='default title')
    text = models.TextField(max_length=3000, null=False)
    image = models.ImageField(upload_to='img/%y')
    date = models.DateField(null=False, auto_now_add=True)

    def __str__(self):
        return f"{self.title} (id: {self.id}, date: {self.date})"


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', null=False, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_comment',
                               null=False, default=None)
    comment = models.TextField(max_length=355, null=False)
    date = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return f"{self.client}`s comment of \"{self.post}\" post (time: {self.date}, id: {self.id}): {self.comment}"
