# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField()),
                ('url', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=225)),
                ('subscribe', models.BooleanField(default='subscribe')),
                ('reason', models.CharField(max_length=225)),
                ('notification_interval', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ManyToManyField(to='treeboapp.User'),
        ),
    ]
