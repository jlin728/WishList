# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0002_auto_20180228_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dob',
            new_name='hired',
        ),
    ]