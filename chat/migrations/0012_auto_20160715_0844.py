# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_chat_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_room',
            name='image',
            field=models.ImageField(null=True, upload_to='chat_room_icons'),
        ),
    ]
