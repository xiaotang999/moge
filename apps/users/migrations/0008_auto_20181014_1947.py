# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-14 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181014_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersetting',
            name='limit_speak_no',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='限制字数'),
        ),
    ]
