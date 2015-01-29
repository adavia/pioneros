# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('team', models.OneToOneField(to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CenterLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('location', models.CharField(max_length=200, blank=True)),
                ('responsable', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('center', models.ForeignKey(to='teams.Center')),
                ('trainers', models.ManyToManyField(to='teams.Directive')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CenterSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_frame', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=1, choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Miercoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'Sabado'), (6, b'Domingo')])),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('center_location', models.ForeignKey(to='teams.CenterLocation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
