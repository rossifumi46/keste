# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_bundle_my'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='my',
            field=models.ManyToManyField(blank=True, related_name='_bundle_my_+', to='core.Bundle'),
        ),
    ]