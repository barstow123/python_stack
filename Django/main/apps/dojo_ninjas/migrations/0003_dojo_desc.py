# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20181015_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
