# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('record_name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('record_logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=25)),
                ('song_title', models.CharField(max_length=50)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Record')),
            ],
        ),
    ]
