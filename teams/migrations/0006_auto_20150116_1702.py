# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_centerlocation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerlocation',
            name='location',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
