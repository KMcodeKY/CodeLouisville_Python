# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20171027_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
