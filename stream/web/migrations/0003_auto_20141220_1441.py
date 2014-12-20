# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20141220_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='stream_team',
            field=models.CharField(default=b'No Team', max_length=240),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='stream_game',
            field=models.CharField(default=b'No Game Selected', max_length=240),
            preserve_default=True,
        ),
    ]
