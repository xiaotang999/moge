# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-14 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersetting',
            options={'verbose_name': '会员组别', 'verbose_name_plural': '会员组别'},
        ),
    ]
