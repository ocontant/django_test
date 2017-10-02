# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('Children_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('RAMQ', models.CharField(blank=True, max_length=14, null=True)),
                ('RAMQ_Expiration', models.DateField(blank=True, null=True)),
                ('Birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('Classe_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Classe_Educator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garderie.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('Educator_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('Phone_emergency', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('Parent_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('Phone_emergency', models.CharField(max_length=15)),
                ('SIN', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Parent_Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Children', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garderie.Children')),
                ('Parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garderie.Parent')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='Childrens',
            field=models.ManyToManyField(related_name='Children', through='garderie.Parent_Children', to='garderie.Children'),
        ),
        migrations.AddField(
            model_name='classe_educator',
            name='Educator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garderie.Educator'),
        ),
        migrations.AddField(
            model_name='classe',
            name='Educators',
            field=models.ManyToManyField(related_name='Educator', through='garderie.Classe_Educator', to='garderie.Educator'),
        ),
    ]
