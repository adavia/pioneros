# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_directive_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='thumbnail1',
        ),
        migrations.AlterField(
            model_name='player',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
