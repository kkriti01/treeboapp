# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeboapp', '0002_auto_20161118_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subscription',
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='product',
            field=models.ManyToManyField(to='treeboapp.Product'),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='reason',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]