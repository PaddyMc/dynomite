# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_auto_20170701_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iduser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='iduser',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
