# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail1',
            field=models.ImageField(null=True, upload_to=b'games/thumbnails/', blank=True),
            preserve_default=True,
        ),
    ]
