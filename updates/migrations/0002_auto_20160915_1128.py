# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-15 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadstatus',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]