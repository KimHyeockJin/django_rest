# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('keyword', models.CharField(max_length=20)),
                ('start_date', models.CharField(max_length=12)),
                ('end_date', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField()),
                ('ratio', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='rest',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hz.Result'),
        ),
    ]
