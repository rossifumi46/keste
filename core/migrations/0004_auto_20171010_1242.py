# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171009_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ManyToManyField(to='core.Room')),
            ],
        ),
        migrations.RemoveField(
            model_name='table',
            name='room',
        ),
        migrations.AddField(
            model_name='table',
            name='bundle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Bundle'),
            preserve_default=False,
        ),
    ]
