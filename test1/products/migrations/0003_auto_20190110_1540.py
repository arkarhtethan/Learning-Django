# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-10 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190110_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=products.models.image_upload_path),
        ),
    ]
