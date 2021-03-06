# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-04 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(default='', verbose_name='içerik')),
                ('publishing_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='yayımlanma tarihi')),
            ],
        ),
    ]
