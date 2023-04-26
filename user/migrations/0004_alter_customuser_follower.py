# Generated by Django 4.1.2 on 2023-04-25 11:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='follower',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]