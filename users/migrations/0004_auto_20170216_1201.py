# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170216_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(help_text='Country Phone Number. E.g +254... ', max_length=12, unique=True),
        ),
    ]