# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-11 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zl955', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guanggao',
            name='is_show',
            field=models.IntegerField(choices=[(False, '不显示'), (True, '显示')], default=0, max_length=2, verbose_name='是否显示'),
        ),
    ]
