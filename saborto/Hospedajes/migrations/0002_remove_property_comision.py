# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospedajes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='comision',
        ),
    ]
