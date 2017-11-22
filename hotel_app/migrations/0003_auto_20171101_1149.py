# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_auto_20171101_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='confort',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='image',
            field=models.CharField(max_length=512, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='services',
            field=models.TextField(blank=True, null=True),
        ),
    ]
