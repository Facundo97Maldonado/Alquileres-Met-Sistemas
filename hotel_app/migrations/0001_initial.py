# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, blank=True, null=True)),
                ('confort', models.CharField(max_length=1024, blank=True, null=True)),
                ('services', models.CharField(max_length=1024, blank=True, null=True)),
                ('maxPax', models.IntegerField(default=1)),
                ('dateFrom', models.DateTimeField()),
                ('dateTo', models.DateTimeField()),
                ('price', models.FloatField(blank=True, default=0)),
                ('image', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(to='hotel_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='host',
            field=models.OneToOneField(related_name='fk_host', to='hotel_app.User'),
        ),
        migrations.AddField(
            model_name='booking',
            name='resident',
            field=models.OneToOneField(related_name='fk_resident', to='hotel_app.User'),
        ),
    ]
