# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-06 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0011_auto_20170306_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gradesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[(b'1', b'Male'), (b'2', b'Female')], default=1, max_length=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradesheet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='user',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
