# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-03-10 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toy',
            options={'ordering': ('created',)},
        ),
    ]