# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171009_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]