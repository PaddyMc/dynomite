# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20170701_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='iduser',
            name='user_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]