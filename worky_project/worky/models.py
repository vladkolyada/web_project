from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="name_order")
    order = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.name} orders:\n" \
               f"{self.order}"


class FeedBack(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="name_fb")
    feedback = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.name} feedback:\n" \
               f"{self.feedback}"

