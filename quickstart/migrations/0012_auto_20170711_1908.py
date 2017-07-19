# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_newiduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='iduser',
            name='email',
            field=models.CharField(default='paddy@paddy.com', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newiduser',
            name='email',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
    ]
