# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0006_auto_20191118_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='schoo_name',
            new_name='school_name',
        ),
        migrations.AlterField(
            model_name='awards',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]