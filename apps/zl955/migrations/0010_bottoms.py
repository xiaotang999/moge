# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-11 15:52
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zl955', '0009_auto_20181011_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='细节')),
                ('explain', models.CharField(help_text='请输入小于200字符的描述！', max_length=250, verbose_name='网站声明')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '底部信息',
                'verbose_name_plural': '底部信息',
            },
        ),
    ]
