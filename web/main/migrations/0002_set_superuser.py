# Generated by Django 3.1.1 on 2020-09-21 08:30
import os

from django.db import migrations
from django.contrib.auth.hashers import make_password


def set_superuser(apps, schema_editor):
    if (email := os.getenv('SUPERUSER_EMAIL')) and (password := os.getenv('SUPERUSER_PASSWORD')):
        user_obj = apps.get_model('main', 'User')
        user = user_obj(
            email=email,
            first_name='Super',
            last_name='Admin',
            is_staff=True,
            is_active=True,
            is_superuser=True,
            password=make_password(password)
        )
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_superuser, migrations.RunPython.noop),
    ]