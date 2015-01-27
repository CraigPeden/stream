# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20141220_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='stream_online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
