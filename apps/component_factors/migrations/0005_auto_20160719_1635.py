# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('component_factors', '0004_auto_20160718_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemoption',
            name='requisites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component_factors.CategoryOption', verbose_name='Category:'),
        ),
    ]
