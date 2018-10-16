# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-16 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip8j888', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='请输入小于200字符的描述！', max_length=250, null=True, verbose_name='地址描述')),
                ('ip', models.CharField(blank=True, max_length=250, null=True, verbose_name='IP地址')),
                ('no', models.IntegerField(blank=True, default=1, null=True, verbose_name='访问次数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '访问IP',
                'verbose_name_plural': '访问IP',
            },
        ),
        migrations.DeleteModel(
            name='IpsApp',
        ),
        migrations.AlterField(
            model_name='agentapp',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='hotapp',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='htmlapp',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AlterUniqueTogether(
            name='ipapp',
            unique_together=set([('ip',)]),
        ),
    ]
