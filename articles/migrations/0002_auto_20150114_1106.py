# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(max_length=200)),
                ('url', models.SlugField(max_length=200)),
                ('link', models.CharField(max_length=200, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'sponsors/', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'sponsors',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='aside',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_title',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
