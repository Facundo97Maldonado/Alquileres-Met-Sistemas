# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0005_auto_20171108_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='estate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rentaldate',
            name='available',
        ),
        migrations.AddField(
            model_name='booking',
            name='number',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='resident',
            field=models.ForeignKey(to='hotel_app.Resident'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='host',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rentaldate',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, to='hotel_app.Booking'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
