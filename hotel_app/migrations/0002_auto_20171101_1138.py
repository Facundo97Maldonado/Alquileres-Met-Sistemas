# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='host',
        ),
        migrations.AddField(
            model_name='booking',
            name='estate',
            field=models.ForeignKey(default=0, to='hotel_app.Estate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estate',
            name='host',
            field=models.OneToOneField(default=0, to='hotel_app.User'),
            preserve_default=False,
        ),
    ]
