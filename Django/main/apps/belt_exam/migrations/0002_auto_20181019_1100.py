# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]
