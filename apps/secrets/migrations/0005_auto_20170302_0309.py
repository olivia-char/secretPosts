# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0004_auto_20170302_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='like',
            field=models.CharField(max_length=250),
        ),
    ]
