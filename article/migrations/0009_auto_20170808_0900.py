# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-08 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20170808_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 8, 9, 0, 37, 848320, tzinfo=utc)),
        ),
    ]
