# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20171004_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='noofmem',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
