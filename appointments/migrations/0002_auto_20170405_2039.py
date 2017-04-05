# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_date',
            new_name='end_datetime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='start_datetime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
    ]
