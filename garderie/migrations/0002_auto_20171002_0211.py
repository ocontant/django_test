# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garderie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='Children_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]