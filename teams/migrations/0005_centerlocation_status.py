# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20150116_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='centerlocation',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
