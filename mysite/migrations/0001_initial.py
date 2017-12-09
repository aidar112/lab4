# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мобильный номер')),
                ('work', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рабочий номер')),
            ],
        ),
    ]