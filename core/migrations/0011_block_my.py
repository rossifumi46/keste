# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171015_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='my',
            field=models.ManyToManyField(blank=True, related_name='_block_my_+', to='core.Block'),
        ),
    ]