# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_password_changed',
            field=models.BooleanField(default=False),
        ),
    ]
