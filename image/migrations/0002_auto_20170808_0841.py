# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-08 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
