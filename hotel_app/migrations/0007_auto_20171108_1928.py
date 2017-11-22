# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0006_auto_20171108_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estate',
            name='dateFrom',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='dateTo',
        ),
    ]
