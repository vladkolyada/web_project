# Generated by Django 4.2.3 on 2023-08-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worky', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='your_email@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='client_feedback', to='worky.client'),
        ),
        migrations.AddField(
            model_name='message',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='client_message', to='worky.client'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=15000),
        ),
    ]
