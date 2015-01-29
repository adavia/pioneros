# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20150116_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerschedule',
            name='day',
            field=models.CharField(max_length=20, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'Sabado', b'Sabado'), (b'Domingo', b'Domingo')]),
            preserve_default=True,
        ),
    ]
