# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_auto_20171101_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
