# Generated by Django 4.2.6 on 2023-10-15 19:09

from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ('ibge', '0002_auto_20231015_1903'),
    ]

    operations = [
        BtreeGinExtension(),
    ]
