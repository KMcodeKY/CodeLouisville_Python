# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('WORK', 'Work'), ('SCHOOL', 'School'), ('SHOPPING', 'Shopping'), ('RESEARCH', 'Research'), ('OTHER', 'Other')], default='OTHER', max_length=255),
        ),
    ]