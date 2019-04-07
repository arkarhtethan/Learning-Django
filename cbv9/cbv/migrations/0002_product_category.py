# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-04 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FOOD', 'Food'), ('DRINK', 'Drink'), ('SNACK', 'Snack'), ('NOODLE', 'Noodle')], default='FOOD', max_length=120),
        ),
    ]