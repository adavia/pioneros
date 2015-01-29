# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_center_centerlocation_centerschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerlocation',
            name='location',
            field=models.CharField(max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='centerschedule',
            name='day',
            field=models.CharField(max_length=1, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'Sabado', b'Sabado'), (b'Domingo', b'Domingo')]),
            preserve_default=True,
        ),
    ]
