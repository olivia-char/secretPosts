# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0003_auto_20170302_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='like',
            field=models.IntegerField(verbose_name=250),
        ),
    ]
