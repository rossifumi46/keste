# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171010_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
