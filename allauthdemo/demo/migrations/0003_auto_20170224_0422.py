# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-24 04:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20170224_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryfine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_fine', to=settings.AUTH_USER_MODEL),
        ),
    ]