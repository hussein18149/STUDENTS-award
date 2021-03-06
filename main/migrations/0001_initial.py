# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('badge', models.ImageField(upload_to='budge')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('username', models.CharField(max_length=60)),
                ('school', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=250)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Award')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
