# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20170406_1544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventMembers',
            new_name='EventMember',
        ),
    ]
