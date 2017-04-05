# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20170405_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_datetime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_datetime',
            field=models.DateField(),
        ),
    ]
