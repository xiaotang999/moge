# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-11 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zl955', '0012_auto_20181011_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipapp',
            name='ip',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='IP地址'),
        ),
    ]
