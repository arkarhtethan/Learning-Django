# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-05 06:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
