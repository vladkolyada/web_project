# Generated by Django 5.0 on 2024-03-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("worky", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]