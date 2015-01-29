# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(max_length=250, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'directives/', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'directives',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('score_local', models.IntegerField(null=True, blank=True)),
                ('score_visitor', models.IntegerField(null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'games',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('sub_title', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('aside', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'history/', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'leagues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'nations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=150)),
                ('nickname', models.CharField(max_length=100, blank=True)),
                ('birth_date', models.DateField()),
                ('height', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('goals', models.IntegerField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'players/', blank=True)),
                ('thumbnail1', models.ImageField(null=True, upload_to=b'players/', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('nationality', models.ForeignKey(blank=True, to='teams.Nation', null=True)),
            ],
            options={
                'verbose_name_plural': 'players',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'positions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'rolls',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=150, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('contact', models.CharField(max_length=100, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'stadiums/', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'stadiums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=b'teams/', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('league', models.ManyToManyField(to='teams.League')),
                ('stadium', models.OneToOneField(to='teams.Stadium')),
            ],
            options={
                'verbose_name_plural': 'teams',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(blank=True, to='teams.Position', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='teams.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='team',
            field=models.OneToOneField(to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(to='teams.League'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='local',
            field=models.ForeignKey(related_name='local_team', to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='visitor',
            field=models.ForeignKey(related_name='visitor_team', to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='directive',
            name='roll',
            field=models.ForeignKey(to='teams.Roll'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='directive',
            name='team',
            field=models.ForeignKey(to='teams.Team'),
            preserve_default=True,
        ),
    ]
