# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20150116_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='team',
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
