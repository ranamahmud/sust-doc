# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-06 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20170306_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std6',
            name='total_lab',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='std6',
            name='total_theory',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
