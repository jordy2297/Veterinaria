# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('dni', models.DecimalField(decimal_places=0, max_digits=8)),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=9)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
