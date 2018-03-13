# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-08 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20180308_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindata',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maindata',
            name='context',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='maindata',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
