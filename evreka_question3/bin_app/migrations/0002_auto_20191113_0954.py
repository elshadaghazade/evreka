# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-13 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bin_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompletedOperations',
            new_name='OperationLog',
        ),
    ]
