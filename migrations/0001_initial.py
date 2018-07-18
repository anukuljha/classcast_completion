# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseblock_index',
            fields=[
                ('block_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=150)),
                ('block_type', models.CharField(max_length=20)),
                ('block_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='user_block_interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('block_number', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classcast_completion.courseblock_index')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='courseblock_index',
            unique_together=set([('course_id', 'block_number')]),
        ),
    ]
