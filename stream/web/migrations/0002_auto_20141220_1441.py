# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream_game',
            field=models.CharField(default=b'No Team', max_length=240),
            preserve_default=True,
        ),
    ]
