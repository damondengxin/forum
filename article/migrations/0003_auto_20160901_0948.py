# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]