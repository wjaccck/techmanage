# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0002_auto_20170726_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='last_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
