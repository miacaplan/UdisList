# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Approved'), (100, 'Unapproved')], default=1),
        ),
    ]
