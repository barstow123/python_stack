# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book_authors.Book'),
        ),
    ]
