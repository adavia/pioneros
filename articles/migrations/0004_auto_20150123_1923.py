# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150114_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='section',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
