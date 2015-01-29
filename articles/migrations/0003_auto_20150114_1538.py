# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150114_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
