# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_house_noofmem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cropping',
            old_name='area',
            new_name='canepercent',
        ),
        migrations.RemoveField(
            model_name='cropping',
            name='crop',
        ),
        migrations.AddField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='companies.Farm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='cornpercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='maizepercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='nutspercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='paddypercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='spicespercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='sunflowerpercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cropping',
            name='wheatpercent',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cropping',
            name='season',
            field=models.CharField(max_length=345, unique=True),
        ),
    ]
