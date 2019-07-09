# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='causal_payload',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='node_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='timestamp',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='key',
            field=models.CharField(max_length=200),
        ),
    ]
