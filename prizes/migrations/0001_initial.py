# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-15 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='articles/')),
                ('bio', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
