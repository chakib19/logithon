# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='validation',
            field=models.BooleanField(default=True),
        ),
    ]
