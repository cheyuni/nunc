# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150308_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(verbose_name='profile', blank=True),
            preserve_default=True,
        ),
    ]
