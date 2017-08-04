# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('crawlerfile', models.FileField(upload_to='./')),
                ('developer', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]