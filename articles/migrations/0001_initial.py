# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('aside', models.TextField()),
                ('url', models.SlugField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.SlugField(max_length=150, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, blank=True)),
                ('description', models.TextField(max_length=200)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/')),
                ('thumbnail1', models.ImageField(null=True, upload_to=b'uploads/thumbnails1/', blank=True)),
                ('thumbnail2', models.ImageField(null=True, upload_to=b'uploads/thumbnails2/', blank=True)),
                ('thumbnail3', models.ImageField(null=True, upload_to=b'uploads/thumbnails3/', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.SlugField(max_length=150, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('url', models.SlugField(max_length=200)),
                ('link', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(max_length=400, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'videos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='articles.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(to='articles.Section'),
            preserve_default=True,
        ),
    ]
