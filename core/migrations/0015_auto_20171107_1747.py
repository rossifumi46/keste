# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_table_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='table', to='core.Block'),
        ),
    ]
