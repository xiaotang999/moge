# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-11 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zl955', '0006_opennew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opennew',
            name='no1',
            field=models.CharField(blank=True, default='0', help_text='请输第1位号码！', max_length=55, null=True, verbose_name='第1位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no2',
            field=models.CharField(blank=True, default='0', help_text='请输第2位号码！', max_length=55, null=True, verbose_name='第2位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no3',
            field=models.CharField(blank=True, default='0', help_text='请输第3位号码！', max_length=55, null=True, verbose_name='第3位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no4',
            field=models.CharField(blank=True, default='0', help_text='请输第4位号码！', max_length=55, null=True, verbose_name='第4位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no5',
            field=models.CharField(blank=True, default='0', help_text='请输第5位号码！', max_length=55, null=True, verbose_name='第5位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no6',
            field=models.CharField(blank=True, default='0', help_text='请输第6位号码！', max_length=55, null=True, verbose_name='第6位'),
        ),
        migrations.AlterField(
            model_name='opennew',
            name='no7',
            field=models.CharField(blank=True, default='0', help_text='请输第7位号码！', max_length=55, null=True, verbose_name='第7位'),
        ),
    ]
