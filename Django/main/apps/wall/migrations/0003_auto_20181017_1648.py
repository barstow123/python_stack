# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-17 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20181017_1645'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Post',
        ),
    ]
