# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20160715_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_room',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
