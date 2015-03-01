# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datadisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(max_length=1),
        ),
    ]
