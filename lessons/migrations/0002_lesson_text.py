# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='text',
            field=models.TextField(default='Insert default here'),
            preserve_default=False,
        ),
    ]
