# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-20 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180518_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
