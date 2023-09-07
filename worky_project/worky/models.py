from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=100, null=False, default="your_email@gmail.com")

    def __str__(self):
        return f"{self.name}({self.email})"


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_message",
                               default=None, null=False)
    message = models.CharField(max_length=15000)

    def __str__(self):
        return (f"{self.client} message:\n"
                f"{self.message}")


class FeedBack(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_feedback",
                               default=None, null=False)
    feedback = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.client} feedback:\n" \
               f"{self.feedback}"

