# Generated by Django 4.2.6 on 2023-10-15 19:03

from django.db import migrations
from django_bm25.operations import Bm25Extension


class Migration(migrations.Migration):

    dependencies = [
        ('ibge', '0001_initial'),
    ]

    operations = [
        Bm25Extension(),
    ]
