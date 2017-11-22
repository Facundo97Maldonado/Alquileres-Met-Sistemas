# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_auto_20171101_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('level', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RentalDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estate',
            name='image',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rentaldate',
            name='booking',
            field=models.ForeignKey(to='hotel_app.Booking'),
        ),
        migrations.AddField(
            model_name='rentaldate',
            name='estate',
            field=models.ManyToManyField(to='hotel_app.Estate'),
        ),
    ]
