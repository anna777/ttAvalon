# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20170405_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_datetime',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_datetime',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=multiselectfield.db.fields.MultiSelectField(default=b'', max_length=5, choices=[(b'1', b'9.00-10.00'), (b'2', b'10.00-11.00'), (b'3', b'11.00-12.00')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=multiselectfield.db.fields.MultiSelectField(default=b'', max_length=5, choices=[(b'1', b'9.00-10.00'), (b'2', b'10.00-11.00'), (b'3', b'11.00-12.00')]),
            preserve_default=True,
        ),
    ]
