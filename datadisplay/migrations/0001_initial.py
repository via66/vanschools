# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_lost', models.DateTimeField(verbose_name=b'date lost')),
                ('color', models.DateTimeField(verbose_name=b'date published')),
                ('breed', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
