# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision_controller', '0002_auto_20171119_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='visiontb',
            name='happen_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]