# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0002_vote_date_voted'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='restaurant',
            field=models.ForeignKey(to='food.Restaurant', related_name='votes'),
        ),
    ]
