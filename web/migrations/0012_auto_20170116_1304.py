# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20161214_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letsencrypt',
            name='last_message',
            field=models.TextField(blank=True),
        ),
    ]
