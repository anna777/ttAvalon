# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20170405_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_datetime',
            field=models.DateTimeField(),
        ),
    ]
