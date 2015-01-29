# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20150120_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, blank=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to=b'games/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('game', models.ForeignKey(to='teams.Game')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
    ]
