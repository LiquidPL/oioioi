# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-17 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paregistration',
            name='terms_accepted',
            field=models.BooleanField(default=False, verbose_name='terms accepted'),
        ),
    ]