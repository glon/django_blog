# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-08 09:11
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20170808_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='images/%Y/%m/%m'),
        ),
    ]
