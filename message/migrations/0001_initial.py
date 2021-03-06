# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 01:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0003_auto_20160905_2253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('0', '已读'), ('1', '未读')], verbose_name='状态')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Comment', verbose_name='被评论的论点')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
    ]
