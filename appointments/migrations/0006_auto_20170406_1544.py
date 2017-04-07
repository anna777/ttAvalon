# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20170405_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('choosed_date', models.DateField()),
                ('choosed_time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='appointments.EventMembers'),
            preserve_default=True,
        ),
    ]
