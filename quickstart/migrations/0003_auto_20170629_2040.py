# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 19:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_topscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='topscore',
            name='date_achieved',
            field=models.DateField(default=datetime.datetime(2017, 6, 29, 19, 40, 44, 576313, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topscore',
            name='score',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
