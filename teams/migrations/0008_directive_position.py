# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150119_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='directive',
            name='position',
            field=models.CharField(default='directive', max_length=100),
            preserve_default=False,
        ),
    ]
