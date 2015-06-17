# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date_voted',
            field=models.DateField(default=django.utils.datetime_safe.date.today, auto_now_add=True),
            preserve_default=False,
        ),
    ]
